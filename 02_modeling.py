import os
import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer


HOUSING_PATH = "datasets/housing"

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing_clean.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
# use SimpleImputer since Imputer will be deprecated in sklearn 0.22
imputer = SimpleImputer(strategy="median")

# drop categorical variables
housing_num = housing.drop("ocean_proximity", axis=1)

# impute using medians
imputer.fit(housing_num)
imputer.statistics_
X = imputer.transform(housing_num)
housing_tr = pd.DataFrame(X, columns=housing_num.columns)

# encode 'ocean_proximity' var
encoder = LabelEncoder()
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
housing_cat_encoded
print(encoder.classes_)

# encoding using OneHot
encoder = OneHotEncoder()
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
housing_cat_1hot

# encoding using LabelBinarizer, which does the previous two steps in combination
encoder = LabelBinarizer()
housing_cat_1hot = encoder.fit_transform(housing_cat)
