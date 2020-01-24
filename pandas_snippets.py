import pandas as pd

steps = pd.read_csv("~/working/datasets/iphone_health/stepsData.csv")
list(steps)
steps = steps.drop(['startDate', 'endDate'], axis=1)
steps['creationDate'] = steps['creationDate'].str.slice(0, 10)
steps = steps.groupby('creationDate', as_index=False).sum()

cycling = pd.read_csv("~/working/datasets/iphone_health/cyclingData.csv")
list(cycling)
cycling = cycling.drop(['startDate', 'endDate'], axis=1)
cycling['creationDate'] = cycling['creationDate'].str.slice(0, 10)
cycling = cycling.groupby('creationDate', as_index=False).sum()


