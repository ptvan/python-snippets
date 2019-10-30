import numpy as np
import pandas as pd
import pymc3 as pm
from matplotlib import pyplot as plt

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