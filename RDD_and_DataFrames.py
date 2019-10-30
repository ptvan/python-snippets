import pandas as pd
import pyspark
from pyspark.sql import SparkSession
import os

# old way for Spark <2.0: start sparkContext, read in CSV as an RDD
sc = pyspark.SparkContext("local", "RDD playground")
rdd = sc.textFile(os.path.join("datasets", "housing", "housing.csv"))
rdd.take(2)
rdd.count()
sc.stop()

# new way with Spark >=2.0, use sparkSession, which encloses a sparkContext
# read CSV in as a DataFrame
sparkSession = SparkSession.builder.appName("DataFrame playground").getOrCreate()
df = sparkSession.read.csv("datasets/housing/housing.csv", header=True)
df.count()
df.columns

df.take(5)

# slightly cleaner tabular output
df.show(5)

# selecting columns or rows
df['longitude','latitude'].show()
df[df.ocean_proximity == 'ISLAND'].show()

# aggregation
df.groupBy('ocean_proximity').count().collect()
df.groupby('ocean_proximity').agg({'median_house_value':'mean'}).collect()

# joining
# NOTE: joining tables do not add prefixes to the column names of the result !
joined = df.join(df2, df2.longitude == df.longitude, `inner`)
joined.toPandas()

sparkSession.stop()

