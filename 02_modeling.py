import os
import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

HOUSING_PATH = "datasets/housing"

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing_clean.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
imputer = SimpleImputer(strategy="Median")


