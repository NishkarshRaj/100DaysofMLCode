# SUPPORT VECTOR REGRESSION
There are two important features of **Support Vector Regression**:
- Hyperplane
- Maximum margin

**Building a SVR:**
- Collect a training set.
- Choose a kernel and it's parameters as well as any regularization needed.
- Form the correlation matrix.
- Train your machine, exactly or approximately, to get contraction coefficients.
- Use those coefficients, create your estimator.
- We use the coeeficients we found during the optimization step and the kernel we started off with.
- Compute the correlation vector.

**In linear regression, we are trying to minimize the errors between the prediction and data. In SVR, _our goal is that the errors do not exceed the threshold_.**

Basically, we are trying to decide a boundary at 'e' distance such that the points closest to the original hyperplane or support vectors are within the boundary lines.

*Hyperplane*---> mx+c=0 <br/>
*Boundary lines*---> mx+c=+e and mx+c=-e [Boundary lines are at a distance e from hyperplane]
