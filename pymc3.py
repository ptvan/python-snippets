import numpy as np
import pandas as pd
import pymc3 as pm
from matplotlib import pyplot as plt
import theano.tensor as tt

#####################
# MODELING STEP COUNTS
#####################

# load step count data which we already cleaned
count_data = pd.read_csv("datasets/apple_health_export/stepsData.csv", sep=",")
count_data = count_data.drop(['creationDate'],1)
count_data['startDate'] = count_data['startDate'].str.slice(0,10)
count_data['endDate'] = count_data['endDate'].str.slice(0,10)
count_data = count_data.groupby(["startDate", "endDate"]).sum()

n_count_data = len(count_data)
plt.bar(np.arange(n_count_data), count_data['stepsWalked'], color="#348ABD")

# create the pymc model
with pm.Model() as model:
    alpha = 1.0 / count_data['stepsWalked'].mean()
    lambda_1 = pm.Exponential("lambda_1", alpha)
    lambda_2 = pm.Exponential("lambda_2", alpha)
    tau = pm.DiscreteUniform("tau", lower=0, upper=n_count_data - 1)

# here we assume there is a day at which the step count changed
with model:
    idx = np.arange(n_count_data)
    lambda_ = pm.math.switch(tau > idx, lambda_1, lambda_2)

# load in our observed step count
with model:
    observation = pm.Poisson("obs", lambda_, observed=count_data['stepsWalked'])

# do the M-H sampling
with model:
    step = pm.Metropolis()
    trace = pm.sample(10000, tune=5000, step=step)

# get the trace for each parameter
lambda_1_samples = trace['lambda_1']
lambda_2_samples = trace['lambda_2']
tau_samples = trace['tau']

# back calculate the number of expected steps, which is
# the sum of all the MCMC samples
N = tau_samples.shape[0]
expected_daily_steps = np.zeros(n_count_data)
for day in range(0, n_count_data):
    ix = day < tau_samples
    expected_daily_steps[day] = (lambda_1_samples[ix].sum() + lambda_2_samples[ix].sum()) / N

# plot it to see when the change occurred
plt.plot(range(n_count_data), expected_daily_steps, lw=4, color="#E24A33", label="expected daily step count")
plt.bar(np.arange(len(count_data)), count_data['stepsWalked'], color="#348ABD", alpha=0.65,
        label="observed step count")

# now do the reverse: generate simulated data using the parameters we obtained
tau = pm.DiscreteUniform.dist(0,2000).random(size=1)
print(tau)

alpha = 1. / 20.
lambda_1, lambda_2 = pm.Exponential.dist(alpha, 2).random(size=2)
print(lambda_1, lambda_2)

data = np.r_[pm.Poisson.dist(lambda_1, tau).random(), pm.Poisson.dist(lambda_2, 2000 - tau).random()]

plt.bar(np.arange(2000), data, color="#348ABD")
plt.bar(tau - 1, data[tau - 1], color="r", label="user behaviour changed")

#####################
# DETECTING CHEATERS
#####################

# generate the true cheaters by sampling from Bernoulli
# note that with pymc 3 the convention is to sample inside a model
# (though we can use pm.Uniform.dist.(params,).random() as well...)

with pm.Model() as model:
    N = 100
    p = pm.Uniform("freq_cheating", 0, 1)
    true_answers = pm.Bernoulli("truths", p, shape=N, testval=np.random.binomial(1,0.5, N))

# the privacy function, where the student flips coins to determine if they are cheaters
with model:
    first_coin_flips = pm.Bernoulli("first_flips", 0.5, shape=N, testval=np.random.binomial(1, 0.5, N))
    second_coin_flips = pm.Bernoulli("second_flips", 0.5, shape=N, testval=np.random.binomial(1, 0.5, N))
    val = first_coin_flips * true_answers + (1 - first_coin_flips) * second_coin_flips
    observed_proportion = pm.Deterministic("observed_proportion", tt.sum(val)/float(N))

# assume we have 35 "Yes" responses
X = 35
with model:
    observations = pm.Binomial("obs", N, observed_proportion, observed=X)

# run the M-H sampling, keeping the traces after the burn-in period...
with model:
    step = pm.Metropolis(vars=[p])
    trace = pm.sample(40000, step=step)
    burned_trace = trace[15000:]

p_trace = burned_trace["freq_cheating"][15000:]
plt.hist(p_trace, histtype="stepfilled", normed=True, alpha=0.85, bins=30,
         label="posterior distribution", color="#348ABD")
