### Project Overview

 Your friend from Iowa, whose housing problem you solved, is now moving to Melbourne for a new assignment Down Under. As you have solved his Iowa housing problem so well, he wants you to solve his Melbourne housing problem too. Armed with your new-found expertise in regularization, let's work on the Melbourne housing data using regularized regression. Each observation is a different house attribute with various features, like the number of properties that exist in the suburb, land size, building size, governing council for the area, real estate agent, price of the house, etc. visualise the data and see if you can help the stakeholders arrive at some inference based on the visual plots.


### Learnings from the project

 Train-test split.

Correlation between the features.

Linear Regression.

Polynomial Regressor.

Lasso Regressor.

Ridge Regressor.

R^2R 
2
 Evaluation Metrics


### Approach taken to solve the problem

 Project Overview |
Data loading and spliting |
Prediction using Linear regression |
Prediction using Lasso |
Prediction using Ridge | 
Prediction using cross validation |
Prediction using polynomial regressor |


### Challenges faced

 Predicting the price of the house using linear regression. Checking the model performance using r^2 scorealso leads to different loan amount distribution by plotting an overlapping density plot of two values.
Predicting the price of the house using a lasso regressor. Checking if there is any improvement in the prediction.
There is very less improvement(~1%), even after applying the regularization and cross-validation score ,perform the prediction using a polynomial regressor to generate second-degree polynomial features.


### Additional pointers

 The dataset has details of 6830 house entries with the following 16 features


