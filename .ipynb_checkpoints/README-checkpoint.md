
## Data Dictionary

1. Credit Limit
    - amount of given credit
2. Gender_M
    - 0: Not Male
    - 1: Male
3. Gender_F
    - 0: Not Female
    - 1: Female
4. Education_College
    - 0: Not college educated (other)
    - 1: College Educated
5. Education_Other
    - 0: College Educated
    - 1: Other
6. Married
    - 0: Other
    - 1: Married
7. Married_Other
    - 0: Married
    - 1: Other
8. Age_Range0
    - 0: If age is not
    - 1: If age is 21-28 Inclusive
9. Age_Range1
    - 0: If age is not
    - 1: If age is 29-34 Inclusive
10. Age_Range2
    - 0: If age is not
    - 1: If age is 35-41 Inclusive
11. Age_Range3
    - 0: If age is not
    - 1: If age is 42-79 Inclusive
12. Pay 1 - Pay 6 [Reverse Order: Sept 2005 is Pay 0, April 2005 is Pay 6]
    - -2: No Consumption
    - -1: Paid in Full
    - 0: The Use of Revolving Credit
    - 1: Payment Delay for One Month
    - 2: Payment Delay for Two Months
    - 3: Payment Delay for Three Months
    - 4: Payment Delay for Four Months
    - 5: Payment Delay for Five Months
    - 6: Payment Delay for Six Months
    - 7: Payment Delay for Seven Months
    - 8: Payment Delay for Eight Months
13. Bill Amount 1-6 [Reverse Order: Sept 2005 is Bill Amount 0, April 2005 is Bill Amount 6]
    - in dollar amounts
14. Pay Amount 1-6 [Reverse Order: Sept 2005 is Pay 0, April 2005 is Pay 6]
    - amount of previous payment
15. Total_Billed_Amt
    - sum of Bill Amount 1-6
16. Total_Pay_Amt
    - sum of Pay Amount 1-6
17. Outstanding_Debt
    - difference of Total_Billed_Amt and Total_Pay_Amt
9. Default 
    - target variable
    - 0 if no 
    - 1 if yes
    


## PipeLine For Our Project


1. Import Our Data
    - read in our data from the given excel file. 
    - split our data into a feature dataframe and a target dataframe
2. Clean And Impute Missing Data
    - we changed our data types of our variables so they were float
    - we found that none of our data was missing, so we did not need to impute anyhting in this step
    - created more features to be used in our data
    - biined Age, Education, Gender, and Marriage
3. Normalize and Standardize Our Data
    - Used the Std Dev to handle outliers on our continous fields
    - Used SciKitLearns normalize function to normalize our data
    - Used MinMax Scaler to then get all of our data between 0 and 1
    - We also had to do more normalizing so we used log() to handle those columns that we still skewed
    - we then added our continous columns back into our initial df
4. Feature Reduction (only for baseline tests)
    - Use RFE Model to select 8 variables
    - Use Correlation to select the top 8 variables
    - Used PCA on our top 8 correlation columns in order to reduce our features further
5. Testing Our Baseline Models
    - we tested our various models using logistic regression and the results are listed below

|     Model    | Auccuracy 
| ------------- |:-------------:|
|  All Features   | .8144 |
| RFE   | . 8159    |
| Correlation   | .8188    |
| PCA | .8185  |

6. Advanced Model Building
We tried various adnvaed models such as Decison Trees, Neural Nets, Auto Encoders, and XGBoost classifiers. All of the models what we built and evaluiated can be found in our Notebooks folder. We ultimately decided to use the XGBoost model to submit as our final model. The results from this can be seen below. We selected this model because we felt that it was the best model overall, when all of our scoring metrics were considered. We also considered the model to be good in terms of fitting (we didn't want to overfit our model). This model can be found in our [Final Model](FinalModel.ipynb) notebook.

|     Precision    | Recall | F1   | Accuracy   | CV Accuracy 
|:----------------:|:------:|:-----:| :--------:| :---------:
|    .79           | .78    | .78  | .78        | .82



7. Contributions

The group leader compiled the code from the other group members into one notebook for submission. We have met several times to work on the project and worked together in order to complete this competition. We each worked on parts of the projects that were in line with our skills and capabilites.  

|     Person    |    Contribution  |
| ------------- |:-------------:|
| Brian            | 40% |
| Kevin          | 30% |
| Ryan          | 30% |

