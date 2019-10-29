import pyspark
import pandas as pd
import os

sc = pyspark.SparkContext("local", "RDD playground")
housing = sc.textFile(os.path.join("datasets", "housing", "housing.csv"))
housing.count()