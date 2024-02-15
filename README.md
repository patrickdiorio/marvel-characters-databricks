Marvel Character Data Analysis

# Description
This project consists of extracting data about Marvel characters using the official Marvel API, processing it at different tiers (Bronze, Silver, Gold) using Databricks, and orchestrating the data flow with Azure Data Factory. The objective is to analyze the frequency of appearance of characters in comics.


# Project Architecture

![image](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/f6a70b04-de73-4525-937b-390c04036697)

# The project design uses medallion architecture:

- Bronze Layer: Raw data extraction from the Marvel API.
- Silver Layer: Data cleaning and structuring for analysis.
- Gold Layer: Data aggregation for high-level insights.

Each layer is implemented as a Databricks notebook and orchestrated by the Azure Data Factory for workflow automation.

# Technologies Used

- Databricks: For data processing and analysis using Spark.
- Azure Data Factory: For data workflow orchestration.
- Azure Key Vault: For secure API key management.
- Marvel API: Source of data about Marvel characters.

# Setup and Installation

## Prerequisites
- Azure account with access to Databricks, Azure Data Factory, and Azure Key Vault.
- Marvel API access keys (public and private).

## Steps
### 1. Azure Key Vault Configuration:
  - Store your Marvel API keys in Azure Key Vault.

![image](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/d7118a57-470e-42a4-8b34-5678d2bc96b9)

### 2. Databricks:
  
  Development of notebooks for the Databricks workspace applying data extraction, cleaning and aggregation.
  - BronzeMarvelCharacters
https://github.com/patrickdiorio/marvel-characters-databricks/blob/98acfc067ded978caa108658affcea1559a7c312/databricks/BronzeLayer/BronzeMarvelCharacters.py

  - SilverMarvelCharacters
https://github.com/patrickdiorio/marvel-characters-databricks/blob/98acfc067ded978caa108658affcea1559a7c312/databricks/SilverLayer/SilverMarvelCharacters.py

 - GoldMarvelCharacters
https://github.com/patrickdiorio/marvel-characters-databricks/blob/98acfc067ded978caa108658affcea1559a7c312/databricks/GoldLayer/GoldMarvelCharacters.py

### 3. Azure Data Factory:
  - Create Linked Service to access Databricks
    
![image](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/db7d01d7-fea9-427c-a5ac-18baaec44f7d)

  - Configure the pipelines to orchestrate the execution of the notebooks in Databricks in the order Bronze → Silver → Gold.

![image](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/469fd8b3-015b-4704-9e56-8ea64d0d8005)

  - Create trigger to update the data pipeline

![image](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/75657f60-c08e-4e36-aadf-048520c69c93)


# Use
Every Monday at 7 am the trigger will run the pipeline in Azure Data Factory. The process is fully automated, from data extraction from Marvel's API to final analysis at the Gold tier.

# Output
- Dashboard
![chart](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/5b3cabee-54af-46d5-a202-bc9af2e74fac)

- Dataset

https://github.com/patrickdiorio/marvel-characters-databricks/blob/cddd849ec897cf9e173cdf8051a6951df3786301/output_gold.characters.csv


