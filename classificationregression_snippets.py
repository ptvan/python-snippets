import sklearn.datasets
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
from scipy import linalg
from sklearn.neighbors import KernelDensity
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn import metrics
from sklearn import mixture
from sklearn.datasets import make_classification
from sklearn.ensemble import AdaBoostClassifier

## import and clean data
steps = pd.read_csv("~/working/datasets/iphone_health/stepsData.csv")
steps = steps.drop(['startDate','endDate'], axis=1)
steps['creationDate'] = steps['creationDate'].str.slice(0,10)
steps = steps.groupby('creationDate', as_index=False).sum()

## Kernel Density Estimation 1D Gaussian
stepsraw = steps['stepsWalked'].to_numpy().reshape(-1,1)
X_plot = np.linspace(-5, 10,1000)[:, np.newaxis]
kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(stepsraw)
log_dens = kde.score_samples(X_plot)
sns.histplot(np.exp(log_dens))

## Random Forest
X, y = sklearn.datasets.load_boston(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

regressor = regressor.estimators_[1]
# output Graphviz .dot file, which needs 
# `dot -Tpng tree.dot -o tree.png '-Gdpi=100'` to convert to PNG
export_graphviz(regressor, out_file='tree.dot', 
                rounded = True, proportion = False, 
                precision = 2, filled = True)


## AdaBoost
X, y = make_classification(n_samples=1000, n_features=4,
                           n_informative=2, n_redundant=0,
                          random_state=0, shuffle=False)
ada = AdaBoostClassifier(n_estimators=100, random_state=0)
ada.fit(X, y)
ada.predict([[0, 0, 0, 0]])
# mean accuracy
ada.score(X, y)

## Gaussian Mixture Model
# NOTE: the data is rather crappy, so errors are expected below.

steps = pd.read_csv("~/working/datasets/iphone_health/stepsData.csv")
steps = steps.drop(['startDate', 'endDate'], axis=1)
steps['creationDate'] = steps['creationDate'].str.slice(0, 10)
steps = steps.groupby('creationDate', as_index=False).sum()

cycling = pd.read_csv("~/working/datasets/iphone_health/cyclingData.csv")
cycling = cycling.drop(['startDate', 'endDate'], axis=1)
cycling['creationDate'] = cycling['creationDate'].str.slice(0, 10)
cycling = cycling.groupby('creationDate', as_index=False).sum()

activity = steps.merge(cycling, 'outer', left_on='creationDate', right_on='creationDate').fillna(0)
X = activity[['stepsWalked', 'milesCycled']]

lowest_bic = np.Infinity
bic = []
n_components_range = range(1,7)
cv_types = ['spherical', 'tied', 'diag', 'full']
for cv_type in cv_types:
    for n_components in n_components_range:
        # Fit a Gaussian mixture with EM
        gmm = mixture.GaussianMixture(n_components=n_components,
                                      covariance_type=cv_type)
        gmm.fit(X)
        bic.append(gmm.bic(X))
        if bic[-1] < lowest_bic:
            lowest_bic = bic[-1]
            best_gmm = gmm
clf = best_gmm

color_iter = itertools.cycle(['navy', 'turquoise', 'cornflowerblue',
                              'darkorange'])

splot = plt.subplot(2, 1, 2)
Y_ = clf.predict(X)
for i, (mean, cov, color) in enumerate(zip(clf.means_, clf.covariances_,
                                           color_iter)):
    v, w = linalg.eigh(cov)
    if not np.any(Y_ == i):
        continue
    plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)

    # Plot an ellipse to show the Gaussian component
    angle = np.arctan2(w[0][1], w[0][0])
    angle = 180. * angle / np.pi  # convert to degrees
    v = 2. * np.sqrt(2.) * np.sqrt(v)
    ell = plt.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
    ell.set_clip_box(splot.bbox)
    ell.set_alpha(.5)
    splot.add_artist(ell)

plt.xticks(())
plt.yticks(())
plt.subplots_adjust(hspace=.35, bottom=.02)
plt.show()