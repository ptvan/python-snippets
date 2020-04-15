import pandas as pd
import numpy as np
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# PCA

dat, x = sklearn.datasets.make_swiss_roll(n_samples=10000, noise=0.05, random_state=500)
princomp = PCA(n_components=2).fit(dat)
print(princomp.explained_variance_ratio_)