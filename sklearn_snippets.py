import sklearn.datasets
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.ensemble import RandomForestRegressor

steps = pd.read_csv("~/working/datasets/iphone_health/stepsData.csv")
steps = steps.drop(['startDate','endDate'], axis=1)
steps['creationDate'] = steps['creationDate'].str.slice(0,10)
steps = steps.groupby('creationDate', as_index=False).sum()

# Kernel Density Estimation 1D Gaussian
stepsraw = steps['stepsWalked'].to_numpy().reshape(-1,1)
X_plot = np.linspace(-5, 10,1000)[:, np.newaxis]
kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(stepsraw)
log_dens = kde.score_samples(X_plot)
sns.distplot(np.exp(log_dens))

# Random Forest
raw = sklearn.datasets.load_boston()
boston = pd.DataFrame(raw.data)
boston.columns = raw.feature_names
