from sklearn.neighbors import KernelDensity
import pandas as pd 
import numpy as np
import seaborn as sns

steps = pd.read_csv("~/working/datasets/iphone_health/stepsData.csv")
steps = steps.drop(['startDate','endDate'], axis=1)
steps['creationDate'] = steps['creationDate'].str.slice(0,10)
steps = steps.groupby('creationDate', as_index=False).sum()

# Kernel Density Estimation
stepsraw = steps['stepsWalked'].to_numpy().reshape(1,-1)
kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(stepsraw)
kde.score_samples(stepsraw)