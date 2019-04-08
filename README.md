
## Data Dictionary

1. Credit Limit
    - amount of given credit
2. Gender (1: Male 2: Female)
3. Education
    - 0: Other
    - 1: Graduate School
    - 2: University
    - 3: High School
    - 4:Other
    - 5:Other
    - 6:Other
4. Marriage
    - 0: Other
    - 1: Married
    - 2: Single
    - 3: Divorced
5. Age
    - age of client
6. Pay 1 - Pay 6 [Reverse Order: Sept 2005 is Pay 0, April 2005 is Pay 6]
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
7. Bill Amount 1-6 [Reverse Order: Sept 2005 is Bill Amount 0, April 2005 is Bill Amount 6]
    - in dollar amounts
8. Pay Amount 1-6 [Reverse Order: Sept 2005 is Pay 0, April 2005 is Pay 6]
    - amount of previous payment
9. Default 
    - target variable
    - 0 if no 
    - 1 if yes
    


## PipeLine For Our EDA

Our Pipline for the Project is as follows:

1. Import Our Data
    - read in our data from the given excel file. 
    - split our data into a feature dataframe and a target dataframe
2. Clean And Impute Missing Data
    - we changed our data types of our variables so they were float
    - we found that none of our data was missing, so we did not need to impute anyhting in this step
3. Normalize and Standardize Our Data
    - Used the Std Dev to handle outliers on our continous fields
    - Used SciKitLearns normalize function to normalize our data
    - Used MinMax Scaler to then get all of our data between 0 and 1
    - We also had to do more normalizing so we used log() to handle those columns that we still skewed
    - we then added our continous columns back into our initial df
4. Feature Reduction
    - Use RFE Model to select 8 variables
    - Use Correlation to select the top 8 variables
    - Used PCA on our top 8 correlation columns in order to reduce our features further
5. Testing Our Models
    - we tested our various models using logistic regression and the results are listed below

|     Model    | Auccuracy 
| ------------- |:-------------:|
|  All Features   | .8144 |
| RFE   | . 8159    |
| Correlation   | .8188    |
| PCA | .8185  |

6. Next Steps
    - we want to try and handle the fact that our target variable, Default, is out of balance.
    - We also created several new variables and binned others, but our models did not improve so we may revisit this and see if there was something we overlooked
    - also want to try more advanced modeling techniques to predict whether someone Defaults
    - we also plan on creating a script to iteratively run through various number of features selected (RFE AND PCA) to evaluae the impact they have on the model. This will save us time from having to try and do each one out manually and will give us a very through view on which model(s) perform the best


7. Contributions

So far we have worked pretty evenly and everyone has been contrbituing to the project. The group leader compiled the code from the other group members into one notebook for submission. We have met several times to work on the project and will continue to do so moving forward as we tweak our models for a better accuracy. 

|     Person    |    Contribution  |
| ------------- |:-------------:|
| Brian            | 40% |
| Kevin          | 30% |
| Ryan          | 30% |

