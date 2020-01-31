import sklearn.datasets
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics

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
X, y = sklearn.datasets.load_boston(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

