# Random Forest Regression
Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks. Random forest is a Supervised Learning algorithm which uses ensemble learning method for classification and regression.
Random forest is a bagging technique and not a boosting technique. The trees in random forests are run in parallel. There is no interaction between these trees while building the trees.

### Feature and Advantages of Random Forest:
**1. It runs efficiently on large databases.
**2. It gives estimates of what variables that are important in the classification.
**3. It is one of the most accurate learning algorithms available. For many data sets, it produces a highly accurate classifier.
**4. It has an effective method for estimating missing data and maintains accuracy when a large proportion of the data are missing.

### Disadvantages of Random Forest :
**1. Random forests have been observed to overfit for some datasets with noisy classification/regression tasks.
**2. For data including categorical variables with different number of levels, random forests are biased in favor of those attributes with more levels. Therefore, the variable importance scores from random forest are not reliable for this type of data.

### Data Set
The given DataSet has 3 columns:
1. Position,
2. Level,
3. Salary.

The Salary is described in accordance to the Position and the Level.
For example if an employee is a Manager — he/she falls in Level 4 and should get around $80,000.

## Importing Libraries
Libraries consists of pre-built functions that take user input and give desired output.

### 1. Importing Libraries in Python

Three essential libraries:

1. numpy: For mathematical functions
2. matplotlib.pyplot: Creating charts for visualization
3. pandas: to import and manage data sets
4. sklearn: To split the dataset and later scaling of test and training data.

### 2. Importing Libraries in R
Can be imported via GUI package explorer in RStudio. Generally all basic libraries we need are automatically imported.

Three essential libraries:

1. caTools: To split the dataset into Training set and Test set.
2. randomForest: Fitting Random Forest Regression to the dataset.
3. ggplot2: To visualize the Random Forest Regression result.

## Implementation in Python

1. Import required libraries.
2. Import and print the dataset.
3. Split the data into training set and test set.
4. Scale the data using StandardScalar.
5. Select all rows and column 1 from dataset to x and all rows and column 2 as y.
x = data.iloc[:, 1:2].values  
print(x) 
y = data.iloc[:, 2].values
6. Fit Random forest regressor to the dataset.
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0) 
regressor.fit(x, y)
7. Predicting a new result
y_pred = regressor.predict(6.5)

8. Visualising the result using pyplot.

## Implementation in R

1. Load the Dataset.
If we look at the dataset, we need to predict the salary for an employee who falls under Level 6.5 — So we really do not need the first column “Position”.
dataset = dataset[2:3]

2. Split the data into training set and test set. Install caTools library to split the data.
3. Scale the training_setand test_set.
4. Fitting Random Forest Regression to the dataset. Install randomForest package.
5. Prediction of new result.
6. Visualization of RFR result in high quality.