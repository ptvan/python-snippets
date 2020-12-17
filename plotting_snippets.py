import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

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
activity.head()

## Matplotlib

# venn diagrams
venn2(subsets = (30, 10, 5), set_labels = ('Group A', 'Group B'))



## Seaborn 

# scatterplot
sns.scatterplot(x="stepsWalked", y="milesCycled", data=activity)

# histogram
sns.distplot(activity['stepsWalked'])
