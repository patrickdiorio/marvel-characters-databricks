# Databricks notebook source
from pyspark.sql.functions import col, current_date
from pyspark.sql.types import IntegerType

# COMMAND ----------

# Table and schema variables
schema = 'gold'
table = 'characters'

# COMMAND ----------

df_characters = spark.sql(
f""" 

    select * from silver.characters

""")

# COMMAND ----------

# Select columns

df_final = df_characters.select(
    col("name").alias("character_name"),
    col("comics_quantity").cast(IntegerType()).alias("quantity_appeared_comics"),
).withColumn('load_date', current_date())

# COMMAND ----------

# Saves the filtered DataFrame in Parquet format, overwriting if the file already exists
df_final \
    .write \
        .format('delta') \
        .mode('overwrite') \
        .option('overwriteSchema', True) \
        .saveAsTable(f'{schema}.{table}')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * 
# MAGIC from gold.characters
# MAGIC order by quantity_appeared_comics desc
