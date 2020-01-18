# Simple Linear Regression

## Introduction

We have a data set having multiple attributes and we want to establish a co-relation amongts each variable.
The simplest data set is one which has only two attribute.
Here, we take a dataset which contains two variables,

1. Years of experience
2. Salary

We want to find the co-relation between above two but we know the default rule of thumb is, 
```
The more is the experience, higher is the expected salary.
```
While this is often true, it depends on the employer, the work you do and many more attributes.

Thus, for accurate prediction, we must populate dataset.

**Most easy way to understand this is in terms of graph between two polar values a,b and y (dependent variable) as a function of independent variables x,y,z ...**
**If the value to be predicted lies between a,b we have a definite analysis but if it goes outside range, we can predict via EXTRAPOLATION**

## Simple Linear Regression

```
Y = mX + c (Regression Formulae)
```
* Y is the Dependent variable
* X is the Independent variable
* C is constant -> intercept of graph when independent variable X is zero 
* Slope -> Multiplier Y depends on X times Y **(UNIT CHANGE)**

**Note: Simple here means that there is only one Independent Variable**

**Note: Linear here means that all independent variables related with dependent variables in ratio of degree 1**

**Note: Simple Linear Regression is used to co-relate dependent variable with the independent variable it depends upon.**

Example: The more a person studies, the more marks he is **likely** to get.

```
LIKELY: Note one thing very seriously that ML algorithm do predictions and not definite solutions. That means they give output that is probable and not 100% guarenteed to be true. 
This is similar to Quantum Mechanics electron in well problem where probability of electron in well is always between 0 and 1
```

Even though the formulae of Simple Linear Regression is same as that of a straight line but it must be noted that dataset when visualized in terms of graph will never give result in form of straight line, it will be approximated as a **BEST FIT** straight line.

## How does Simple Linear Regression model create "Best Fitting Line" or "Trend Line" from actual data set? == Ordinary Square Method

For each value of Xi (Independent value), multiple lines can be created using different M and C values.
For each actual value (Yi) and modelled value (Yi^), calculate the SUM of (yi-yi^)^2 and choose the best fitting line which has minimum square value.

