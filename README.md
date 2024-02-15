Marvel Character Data Analysis

# Description
This project consists of extracting data about Marvel characters using the official Marvel API, processing it at different tiers (Bronze, Silver, Gold) using Databricks, and orchestrating the data flow with Azure Data Factory. The objective is to analyze the frequency of appearance of characters in comics.


# Project Architecture

![image](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/f6a70b04-de73-4525-937b-390c04036697)

# The project follows a layered data processing approach:

- Bronze Layer: Raw data extraction from the Marvel API.
- Silver Layer: Data cleaning and structuring for analysis.
- Gold Layer: Data aggregation for high-level insights.
- 
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
1. Azure Key Vault Configuration:
- Store your Marvel API keys in Azure Key Vault.

2. Databricks:
- Development of notebooks (Bronze, Silver, Gold) for the Databricks workspace applying data extraction, cleaning and aggregation.

3. Azure Data Factory:
- Configure the pipelines to orchestrate the execution of the notebooks in Databricks in the order Bronze → Silver → Gold.


# Use
Activate the trigger that will run the pipeline in Azure Data Factory. The process is fully automated, from data extraction from Marvel's API to final analysis at the Gold tier.

![chart](https://github.com/patrickdiorio/marvel-characters-databricks/assets/86168049/5b3cabee-54af-46d5-a202-bc9af2e74fac)

