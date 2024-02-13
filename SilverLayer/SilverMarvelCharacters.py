# Databricks notebook source
from pyspark.sql.functions import col, current_date

# COMMAND ----------

# Table and schema variables
schema = 'silver'
table = 'characters'

# COMMAND ----------

df_characters = spark.sql(
f""" 

    select * from bronze.characters

""")

# COMMAND ----------

df_final = df_characters.select(
    col("id"),
    col("name"),
    col("description"),
    col("comics.available").alias("comics_quantity"),
    col("events.available").alias("events_quantity"),
    col("series.available").alias("series_quantity"),
    col("stories.available").alias("stories_quantity"),
    col("modified")
).withColumn('load_date', current_date())

# COMMAND ----------

# Saves the filtered DataFrame in Parquet format, overwriting if the file already exists
df_final.write.format('delta').mode('overwrite').option('overwriteSchema', True).saveAsTable(f'{schema}.{table}')
