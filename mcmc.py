import numpy as np
import pandas as pd
import pymc3 as pm

count_data = pd.read_csv("datasets/apple_health_export/stepsData.csv", sep=",")
count_data = count_data.drop(['creationDate'],1)
count_data['startDate'] = count_data['startDate'].str.slice(0,10)
count_data['endDate'] = count_data['endDate'].str.slice(0,10)
count_data = count_data.groupby(["startDate", "endDate"]).sum()


n_count_data = len(count_data)

with pm.Model() as model:
    alpha = 1.0 / count_data['stepsWalked'].mean()
    lambda_1 = pm.Exponential("lambda_1", alpha)
    lambda_2 = pm.Exponential("lambda_2", alpha)
    tau = pm.DiscreteUniform("tau", lower=0, upper=n_count_data - 1)

with model:
    idx = np.arange(n_count_data)
    lambda_ = pm.math.switch(tau > idx, lambda_1, lambda_2)

with model:
    observation = pm.Poisson("obs", lambda_, observed=count_data['stepsWalked'])

with model:
    step = pm.Metropolis()
    trace = pm.sample(10000, tune=5000, step=step)

lambda_1_samples = trace['lambda_1']
lambda_2_samples = trace['lambda_2']
tau_samples = trace['tau']