import pandas as pd
import seaborn as sns
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
sns.distplot(activity['stepsWalked'])
