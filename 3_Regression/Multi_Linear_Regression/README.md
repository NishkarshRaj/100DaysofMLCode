## Business problem description

We are provided with a data set with N independent variables (N>1) and 1 dependent variables. 
We have to find the relationship between dependent variable and all independent variables combined.

**Example:** One of the biggest example for this is IT companies. 

Given a dataset of companies with following independent variables:
1. Headquarter location
2. Capital spent on Research
3. Capital spent on Administration
4. Capital spent on Marketing the product.

We have to find the profit based on all independent variable combined.

## Multi Linear Regression

```
Y = m0 + m1X1 + m2X2 + m3X3 + ... + mNXN
```

* **Linear Regression:** Dependent variable related with independent variable in first order only.
* **Multi:** More than one independent variable

## Assumptions of Linear Regression

1. Linearity
2. Independence of errors
3. Homoscedasticity
4. Multivariate normality
5. Lack of multi collinearity

## Dummy Variables: 

**Need of Dummy variables:** When creating an equation for multi linear regression model, we must understand that the equation only includes numeric values and thus we have to convert variables with string inputs into categorical dummy variables.

**Dummy variables for categorical data work as switches:** A dummy variable can be only in one of all categories at once. Thus, dummy variables work as switches, they can either be 1 or 0 only.


**Dummy Variable Trap**
If we have N categories and N corresponding dummy variables, we should not include all the dummy variables in our final equation because it creates an overhead.
Example: If we have only two dummy variables, we should take only one variable because if the variable has value 0 that implies that other variable has value 1.
The variables that are not included in our final multi linear regression model equation are considered to be default condition and they are handled by the constant part of our equation.

The Dummy Variable Trap means that we should never include all the dummy variables and the constant value together in our equation because the machine cannot distinguish between these related values due to **multi collinearity** which increases the overhead and decreases the accuracy of our model.

**Rule of thumb:** Always exclude one or more irrelevant dummy variables from our Multi Linear Regression equation.

## Building Multi Linear Regression Model

**Pre-requisite:** For n independent variables, we have to remove some of the independent variables that are not of high importance or priority because of following reasons:
**1. Complexity:** Higher the number of independent variables, the poor will be the performance of our machine
**2. Accuracy:** If number of low priority variables are high, it might decrease the accuracy of the machine.

There are five methods of building the model for Multi Linear Regression:
1. All-in
2. Backward Elimination
3. Forward Selection
4. Bidirection Elimination
5. Score Comparision

