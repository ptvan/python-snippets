import pyspark
from pyspark.sql import SQLContext
import pandas as pd
import os

sc = pyspark.SparkContext("local", "RDD playground")

# read in CSV as an RDD
housing = sc.textFile(os.path.join("datasets", "housing", "housing.csv"))
housing.take(2)
housing.count()

# alternatively, create a DataFrame
sqlContext = SQLContext(sc)
housingDF = sqlContext.read.csv("datasets/housing/housing.csv", header=True)
housingDF.take(2)
housingDF.count()
