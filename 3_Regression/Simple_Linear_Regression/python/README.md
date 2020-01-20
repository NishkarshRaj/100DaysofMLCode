# Simple Linear Regression in Python

## Part 1: Data Pre-Processing

**1. Import the libraries**

**2. Import the Dataset**
* Import dataset in our working directory
* Divide data set into Independent variable matrix (X) and dependent variable matrix (Y)

**3. Split data into test and train set**

```
Note: Significance of Train and Test Data
Machine Learning model learns about co-relations between Independent variable in Train data set with its Dependent variable.
Then, be working on Test Data independent variables, it predicts the dependent variable values.
Then the test data predicted and observed values are compared to check accuracy of the Machine Learning models.
```

**Note: Feature Scaling is not necessary for Simple Linear Regression**

## Part 2: Embed Linear Regression model in our dataset and fit it to the training data set

```python
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(Independent_Train_data_matrix, Dependent_Train_data_matrix)
```

* Line 1: Import **sklearn.linear_model** library and import **LinearRegression** class.
* Line 2: Create regressor object of LinearRegression class.
* Line 3: Fit this object to training data set to find co-relations between the Independent and Dependent variable matrix.

Now, our machine has **learnt** the correlations between the dependent and independent data matrix and is now capable of predicting the dependent values on independent test data set.

## Part 3: Creating prediction vector of Dependent variable of test data

```python
pred_vector = regressor.predict(X_test)
```

It creates **predicted values** for test data that can be compared with the **True/observed values** of test data which can show the accuracy of our Machine Learning model.
