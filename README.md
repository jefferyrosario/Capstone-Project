# Capstone Project


## Introduction

This repository contains my Capstone Project, an analysis and classfication of the success rate of clinical trials. 


### Problem Statement

Company A is dedicated to bringing down the cost and improving the outcomes of the drug discovery pipeline. As such we are very interested in understanding the drivers behind successful and unsuccessful clinical trials. Company A seeks to use machine learning to evaluate the use of machine learning models in prediction the success rate of clinical trials. Can we use the clinical trials reference papers to enhance our predictive models?


## Contents

 
tokens/                   - Directory containing the tokens for PMIDs

list_of_PMIDs0-29.csv     - Excel spreadsheet split into 29 sheets to run python script in parallel

fetch_pdfs.py             - Python script to scrape .pdfs. Credits to https://github.com/billgreenwald/Pubmed-Batch-Download/blob/master/fetch_pdfs.py

df.pkl                    - Saved DataFrame




## Summary

1. This exploration involved downloading the clinical trials from clinicaltrials.gov. Clinical trials art identified through their NCT ids. All clinical trials are given in the XML format. You can use beautifulSoup to parse out the data you will use for analysis. Each clinical trial will also have PMIDs, PubMed identification numbers, for each NCT_id.

2. Use fetch_pdfs.py on the selected PMIDs to download the pdfs. There may be a paywall so there will be problems downloading all of the necessary pdfs

3. Exploratory data analysis. Understand the data. Find the numerical, categorical, and text data. Find the target variables. 

4. Create a baseline model. Improve on the model and try different parameters. We used a Logistic Regression and Kfold cross validation in finality.

5. Get a classification report. Determine if the precision or recall is more important in this scenario. Precision of the Success variable was the most important in this case.




## Conclusion

We were able to see modest improvements of the Logistic Regression with the inclusion of PMIDs. Overall accuracy of around 83% and precision score of 66%.
