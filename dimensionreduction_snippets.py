import pandas as pd
import numpy as np
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from sklearn import cluster

dat, x = sklearn.datasets.make_swiss_roll(n_samples=10000, noise=0.05, random_state=500)

# PCA
princomp = PCA(n_components=2).fit(dat)
print(princomp.explained_variance_ratio_)

# MDS
multidim = MDS(n_components=2).fit_transform(dat)

# Feature agglomeration
agglo = cluster.FeatureAgglomeration(n_clusters=3)
agglo.fit(dat)
dat_reduced = agglo.transform(dat)