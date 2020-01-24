# Polynomial Linear Regression

In Polynomial Regression, there is only one independent variable but its effect is multi fold with multiple degrees of it affecting the dependent variable.

```
Y = c0 + c1*x1 + c2*x1^2 + c3*x1^3 + ... cN*x1^N
```

**Polynomial Regression is linear because the order of an equation depends upon the unknown values and here co-efficients and not the independent value is unknown.**

**Note:** Polynomial regression is a type of Multi Linear Regression.

## Data set explanation:

Earlier we handled the one independent - one dependent variable problem in the Simple Linear Regression model where the two variables were linearly dependent on each other but sometimes, the relation between the variables is non-linear.

In the example taken here, irrespective of the experience, the salary given wrt position of the employee is non-linear.
Considering jump from one position to successive position takes constant years, we have to predict salary of each employee in the transition period becuase we expect salary to increase annualy in range between current position salary and next position salary.
