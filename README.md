# Project 2 - Ames Housing Data and Kaggle Challenge

---

## Project Challenge Statement

### Goal: Predict the price of homes at sale for the Aimes Iowa Housing dataset. 

Two files are provided to build the model. 

- train.csv -- this data contains all of the training data for your model.
The target variable (SalePrice) is removed from the test set!
- test.csv -- this data contains the test data for your model. You will feed this data into your regression model to make predictions.

## Table of Contents

This Notebook is broken down into different sections for analysis purpose. The following links are connected to different section within the Notebook for simple navigation.

### Contents 

- [01_EDA_And_Data_Cleaning](https://git.generalassemb.ly/evolevelynli/project_2/blob/master/code/01_EDA_And_Data_Cleaning%20.ipynb) 
- [02_Data_Preprocessing](https://git.generalassemb.ly/evolevelynli/project_2/blob/master/code/02_Data_Preprocessing.ipynb) 
- [03_Model_Benchmarks](https://git.generalassemb.ly/evolevelynli/project_2/blob/master/code/03_Model_Benchmarks.ipynb) 
- [04_Model_Tuning](https://git.generalassemb.ly/evolevelynli/project_2/blob/master/code/04_Model_Tuning.ipynb)
- [05_Production_Model_and_Insights](https://git.generalassemb.ly/evolevelynli/project_2/blob/master/code/05_Production_Model_and_Insights.ipynb)

## The Modeling Process

1. EDA and Data Cleaning
    - Sale Price Trend
    - 42 Categorical Features and 39 Numerical Features
    - Numeric null -> mean, Categorical Null -> None
2. Numerical Features Extraction
    - Run Linear Regression with all numeric features
    - Select the ones with p-values less than 0.05
3. Bench Mark Models (dummies and selected numerical features, polynomial transformation, standardization of X)
    - Linear Regression
    - Ridge Regression
    - Lasso Regression
    - Elastic Net Regression
4. Model Tuning (dummies and selected numerical features, polynomial transformation, standardization of X and Y)
    - Key Features Selection
5. Select variables with high coefficients in Lasso Model
    - Run Linear Regression with selected variables and extract the features with p-value < 0.05

## Key Variables For Predicting Sale Price 

- 2nd Flr SF                            
- Overall Qual Year Built               
- Overall Qual                          
- Lot Frontage Screen Porch             
- 1st Flr SF                            
- 2nd Flr SF Neighborhood_StoneBr       
- 2nd Flr SF Garage Cond_Ex             
- Lot Area Overall Cond                 
- Total Bsmt SF Neighborhood_StoneBr    
- BsmtFin SF 1 Total Bsmt SF            
- Year Built                            
- Overall Cond Neighborhood_StoneBr     
- BsmtFin SF 1 Neighborhood_OldTown     
- Year Built Bedroom AbvGr              
- Total Bsmt SF Garage Area             
- Total Bsmt SF Neighborhood_NridgHt    
- Lot Frontage Lot Area                 
- BsmtFin SF 1 Neighborhood_NoRidge     
- Neighborhood_Sawyer                   
- Bedroom AbvGr Neighborhood_NridgHt    
- Overall Cond Exterior 1st_BrkFace     
- 1st Flr SF Neighborhood_NAmes         
- 1st Flr SF Neighborhood_NoRidge       
- Mas Vnr Area 2nd Flr SF               
- Overall Qual Neighborhood_Sawyer      
- Lot Area                              
- Overall Cond Neighborhood_NridgHt     
- Lot Area Year Built                   
- Lot Frontage Bedroom AbvGr            
- 1st Flr SF Neighborhood_Sawyer        


## Recommendation

According to our analysis, there are few variables have a significantly high positive correlation with the Sale Price of one's house. First is the overall condition of the house. The p-value of an overall condition variable is less than 0.05 which means we will reject the null hypothesis of saying there is no relationship between overall condition and sale price. As the overall condition of the house increases, the sale price of the house increase as well. Meanwhile, Lot area, Lot Frontage Lot Area, square foot first and second floor of the house also have a high correlation with the Sale Price. In other words, the larger the space of the home is, the higher the sale price will be. Another essential feature that contributes to an increase in sale price is overall quality with year built. If a house is built recently, and the quality of the house is good, the sale price of the home will be higher. 

Within the features that have low p-values, few variables such as 2nd Flr SF Neighborhood_StoneBr, Total Bsmt SF Neighborhood_NridgHt, Overall Qual Neighborhood_Sawyer, and Total Bsmt SF Neighborhood_NWAmes point us to the direction of understanding the importance of location. Especially variable Neighborhood_Sawyer, which has a positive correlation with Sale Price, means that if your house is in this neighborhood, the Sale Price of the home will go up. Another interesting thing to notice for these interaction variables is that some specific house features in different locations can boost the sale value of a home if the home fulfills both qualities. For example, the interaction term 2nd_Flr_SF_Neighborhood_StoneBr means that the house has a second floor and its location is in Stone Brook. The way we can interpret this variable that if a home locates at Stony Brook, as the square footage of the home's second-floor increases, the sale price increases as well. 

As for the features that decrease the Sale Price of the house, One interaction term caught my eye: Lot_Frontage_Bedroom_AbvGr, which is an interaction term between Lot Frontage and number of bedrooms above ground. This interaction term is significant and has a negative relationship with the Sale Price. However, we can't draw any conclusion about lot frontage and bedroom only base on this one variable. This negative relationship between the interaction term and sale price could be compensation to adjust the real relationship between variables since both Lot Frontage and Bedroom above ground have a positive correlation with the sale price. From this variable, we can say that some of the variables in the regression model are not quite explanatory on its own. 

Based on the analysis above, we will provide the following business recommendation for those who are interested in boosting their house sale price. First, homeowners must understand the importance of location.  Some neighborhoods are better than others thus have a higher value on their homes. If one is interested in raising housing value in a particular neighborhood, we can perform further analysis by extracting information based on the specific area to understand what are some of the key features that contribute to sale price in this particular neighborhood. However, for everyone else who already has a house and looking forward to improving the sale price regardless of location, there are things you can do. If your home has a second floor, this feature only will add value to your sale price. If you do not have a second floor, there are ways for you to improve profits by improving the overall condition of your house. Depends on the status of the house, there are a variety of things you can do to increase the value of your home quickly. Before selling the home, homeowners should identify the area in the house that needs fixing up and fix up the part that will give the house the most significant value boost. For example, painting your walls will not cost you so much, but it will increase the value of the home significantly because your house now will look cleaner and newer than before. After all, the quality of the house is crucial for buyers.  