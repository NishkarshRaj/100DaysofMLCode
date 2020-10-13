""" XGBoost

Install xgboost following the instructions on this link: http://xgboost.readthedocs.io/en/latest/build.html#
"""

# Importing the libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
import xgboost as xgb

def main():
    # Importing the dataset
    dataset = pd.read_csv('Churn_Modelling.csv')
    X = dataset.iloc[:, 3:13].values
    y = dataset.iloc[:, 13].values

    # Encoding categorical data
    labelencoder_X_1 = LabelEncoder()
    X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
    labelencoder_X_2 = LabelEncoder()
    X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
    onehotencoder = OneHotEncoder(categorical_features=[1])
    X = onehotencoder.fit_transform(X).toarray()
    X = X[:, 1:]

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Fitting XGBoost to the Training set
    classifier = xgb.XGBClassifier()
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    # Applying k-Fold Cross Validation
    accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10)
    accuracies.mean()
    accuracies.std()


if __name__ == '__main__':
    main()
