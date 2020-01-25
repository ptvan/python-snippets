import sklearn
import pandas as pd 

steps = pd.read_csv("~/working/datasets/iphone_health/stepsData.csv")
steps = steps.drop(['startDate','endDate'], axis=1)
steps['creationDate'] = steps['creationDate'].str.slice(0,10)
steps = steps.groupby('creationDate', as_index=False).sum()