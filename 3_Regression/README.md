## Regression Techniques

[1. Simple Linear Regression](Simple_Linear_Regression)
  
[2. Multi Linear Regression](Multi_Linear_Regression)
  
[3. Polynomial Regression](Polynomial_Regression)

[4. Support Vector Regression](Support_Vector_Regression)

[5. Decision Tree Regression](Decision_Tree_Regression)

[6. Random Forest Regression](Random_Forest_Regression)

## Comparing Regression Models and their performance

**R Squared Intution for Simple Linear Regression**

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

