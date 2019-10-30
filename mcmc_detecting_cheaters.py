import scipy.stats as stats
import pymc3 as pm
import numpy as np
import theano.tensor as tt
import matplotlib as plt

# generate the true cheaters by sampling from Bernoulli
# note that with pymc 3 the convention is to sample inside a model
# (though we can use pm.Uniform.dist.(params,).random() as well...)

with pm.Model() as model:
    N = 100
    p = pm.Uniform("freq_cheating", 0, 1)
    true_answers = pm.Bernoulli("truths", p, shape=N, testval=np.random.binomial(1,0.5, N))

# the privacy function, where the student flips coins to determine
# if they are cheaters
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