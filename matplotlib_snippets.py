import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

steps = pd.read_csv("~/working/datasets/iphone_health/stepsData.csv")
list(steps)
steps.shape
steps.head()
steps = steps.drop(['startDate', 'endDate'], axis=1)
steps['creationDate'] = steps['creationDate'].str.slice(0, 10)
steps = steps.groupby('creationDate', as_index=False).sum()

cycling = pd.read_csv("~/working/datasets/iphone_health/cyclingData.csv")
list(cycling)
cycling.shape
cycling.head()
cycling = cycling.drop(['startDate', 'endDate'], axis=1)
cycling['creationDate'] = cycling['creationDate'].str.slice(0, 10)
cycling = cycling.groupby('creationDate', as_index=False).sum()

activity = steps.merge(cycling, 'outer', left_on='creationDate', right_on='creationDate').fillna(0)
activity.rename(columns={"creationDate" : "date"})

%matplotlib inline

# barplot with 2 X-axes
t = np.arange(activity.shape[0])
fig, ax1 = plt.subplots()

ax1.set_xlabel('day')
ax1.set_ylabel('stepsWalked', color="red")
ax1.plot(t, activity['stepsWalked'], color="red")
ax1.tick_params(axis='y', labelcolor="red")

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('milesCycled', color="blue")  # we already handled the x-label with ax1
ax2.plot(t, activity['milesCycled'], color="blue")
ax2.tick_params(axis='y', labelcolor="blue")

fig.tight_layout()

# scatterplot 
fig, ax = plt.subplots()
ax.scatter(activity['stepsWalked'], activity['kcalBurned'])
ax.grid(True)
ax.set_xlabel('stepsWalked', color="black")
ax.set_ylabel('kcalBurned', color="black")
