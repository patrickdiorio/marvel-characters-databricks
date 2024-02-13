# Databricks notebook source
import requests
import hashlib
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date

# COMMAND ----------

# Recovers keys from Azure Key Vault
public_key = dbutils.secrets.get(scope="scope-databricks", key="MarvelPublicKey")
private_key = dbutils.secrets.get(scope="scope-databricks", key="MarvelPrivateKey")

# Timestamp
timestamp = str(time.time())

# Generate MD5 hash as part of the authentication parameters
hash_value = hashlib.md5((timestamp + private_key + public_key).encode('utf-8')).hexdigest()

# Table and schema variables
schema = 'bronze'
table = 'characters'

# COMMAND ----------

# URL to access API
url = "http://gateway.marvel.com/v1/public/characters"

# API call parameter configuration
params = {
    'apikey': public_key,
    'ts': timestamp,
    'hash': hash_value,
    'limit': 100 
}
# GET request to the API with the authentication parameters.
response = requests.get(url, params=params)

# Convert the API response from JSON to a Python dictionary
characters_data = response.json()['data']['results']

# COMMAND ----------

# Start a Spark session
spark = SparkSession.builder.appName("MarvelCharacters").getOrCreate()

# Creates a Spark DataFrame from API results
df_characters = spark.createDataFrame(characters_data)

# COMMAND ----------

# Select columns

df_final = df_characters.select(
    col("comics"),
    col("description"),
    col("events"),
    col("id"),
    col("modified"),
    col("name"),
    col("resourceURI"),
    col("series"),
    col("stories"),
    col("thumbnail"),
    col("urls")
).withColumn('load_date', current_date())

# COMMAND ----------

# Saves the filtered DataFrame in Parquet format, overwriting if the file already exists
df_final \
    .write \
        .format('delta') \
        .mode('overwrite') \
        .option('overwriteSchema', True) \
        .saveAsTable(f'{schema}.{table}')
