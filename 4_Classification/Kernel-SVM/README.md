#Kernel-SVM

SVMs (Support Vector Machines) are a set of tools used for supervised machine learning. The SVM "draws" a boundary between the separated classes by maximizing the distance to the nearest points of both classes. You can find the documentation here in the [scikit-learn library](https://scikit-learn.org/stable/modules/svm.html).

Compared to Naive Bayes, SVMs are more flexible, as you can modify parameters to modify the separator boundary (by "drawing" linear lines, curves or wiggly fields ) or to tolerate outliers.

## 1 initialize and train the SVM in Python
'''
>>> from sklearn import svm
>>> X = [[0, 0], [1, 1]]
>>> y = [0, 1]
>>> clf = svm.SVC()
>>> clf.fit(X, y)
SVC()
'''


## 2 Predict Values with the SVM in Python
'''
>>> clf.predict([[2., 2.]])
array([1])
'''

## 3 Adjust the models fit by changing parameters in Python
There are various parameters that can be defined for a better fit of the model. See the [documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC) here. The 3 most important are:

Change the Kernel to make the separator boundary linear or curvy. Possible kernels are e.g. linear, rbf, polynomial and more.
'''
>>> clf = svm.SVC(kernel="linear")
'''

Change the C parameter to control the tradeoff between drawing a smooth decision boundary vs. classifying training points correctly. The smaller the C the straigther the boundary becomes (and fewer points are classified correctly).
'''
>>> clf = svm.SVC(C=1.0)
'''

Change the gamma parameter to define how far the influence of a single training point reaches. With high gamma values, only the nearest points are considered (and outliers are rather ignored), with low gamma also the far reaching points are considered.
'''
>>> clf = svm.SVC(gamma=1000)
'''
