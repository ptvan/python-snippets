###########################
# RDDs and Spark DataFrames
###########################

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
# NOTE: joining Spark DataFrames do not add prefixes to the column names of the result !
# so will need to rename columns
joined = df.join(df2, df2.longitude == df.longitude, "inner")

# this needs to be small enough to fit into driver's memory...
joined.toPandas()

# write out to various formats
joined.write.save("housing.parquet", format="parquet")
joined.write.save("housing_new.csv", format="csv")

# SQL interface
# we must create a view
df.createOrReplaceTempView("df")
sparkSession.catalog.listTables()
sparkSession.sql("SELECT * FROM df").show()

# alternatively, we can take an existing Pandas DataFrame
# and convert it to a Spark DataFrame

pdf = pd.read_csv("datasets/housing/housing.csv")
tmp_df = sparkSession.createDataFrame(pdf)
tmp_df.createOrReplaceTempView("df")

# this replaced the previous 'df' in the catalog!
sparkSession.catalog.listTables()

sparkSession.stop()