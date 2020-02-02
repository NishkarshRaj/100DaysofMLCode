## Regression Techniques

[1. Simple Linear Regression](Simple_Linear_Regression)
  
[2. Multi Linear Regression](Multi_Linear_Regression)
  
[3. Polynomial Regression](Polynomial_Regression)

[4. Support Vector Regression](Support_Vector_Regression)

[5. Decision Tree Regression](Decision_Tree_Regression)

[6. Random Forest Regression](Random_Forest_Regression)

## Comparing Regression Models and their performance

### R Squared Intution for Simple Linear Regression

Simple Linear Regression Model is based on mathematical model with following condition
```
Take line that has minimum value of SUM(Yobserved-Ypredicted)^2
```

Here, **SUM(Yobserved-Ypredicted)^2** can be termed as **Sum of Residuals**.

Rather than choosing our models based on Minimum residual sum, we can make a better model by comparing the different regressors with average regressor (Yavg = Sum(Yobserved)/N(Y))
Sum of Residuals for Average regressor is called **Sum of Totals**

```
R^2 = 1 - (Sresidual/Stotal)
```

* It can be inferenced that R square can never be greater than 1.
* If R square is less than one, the regressor is not a good model.
* Since we have to minimize Sum Residual, R square must be maximized.
* Thus, if R^2 is closer to 1, the model is good and vice versa.

### Adjusted R Squared Intution

**Problem in R Square method:** It cannot predict whether increasing number of independent variables improve or degrade our model.
**Reason:** R square never decreases, it can only increase or remain constant. 
> Increase: 1 and Stotal are constant, if model improves, Sres decreases and the R square increases

> Constant: Adding new variable has negligible impact and Sres is practically same as old.

Thus, we can never state whether adding new variables improve or degrade our model because R2 equation does not depend on number of variables

**Adjusted R Square Model**
```
Adjusted R Square = 1 - [(1-R^2)*(n-1/n-p-1)]
```
* p = number of regressors/number of independent variables
* n = sample size (constant for dataset)

Here, p is the penalization factor and has opposite effect to R^2 value.
> Effect of p: Increasing number of independent variables decreases the value of Adjusted R square

> Effect of R square: R square can only increase, so increase in it increases Adjusted R square

**Note:** On adding new variable, if Adjusted R^2 increases, keep the new variable else discard it.
