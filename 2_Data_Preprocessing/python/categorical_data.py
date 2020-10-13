""" Data Preprocessing
"""

# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def main():
    # Importing the dataset
    dataset = pd.read_csv('../Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 3].values

    # Taking care of missing data
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer = imputer.fit(X[:, 1:3])
    X[:, 1:3] = imputer.transform(X[:, 1:3])

    # Encoding categorical data
    # Encoding the Independent Variable
    labelencoder_X = LabelEncoder()
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
    onehotencoder = OneHotEncoder()
    X = onehotencoder.fit_transform(X).toarray()
    # Encoding the Dependent Variable
    labelencoder_y = LabelEncoder()
    y = labelencoder_y.fit_transform(y)


if __name__ == '__main__':
    main()
