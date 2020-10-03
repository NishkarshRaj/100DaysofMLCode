""" Data Preprocessing
"""

# Importing the libraries
import pandas as pd
from sklearn.impute import SimpleImputer


def main():
    # Importing the dataset
    dataset = pd.read_csv('../Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 3].values

    # Taking care of missing data
    imputer = SimpleImputer(missing_values='NaN', strategy='mean')
    imputer = imputer.fit(X[:, 1:3])
    X[:, 1:3] = imputer.transform(X[:, 1:3])


if __name__ == '__main__':
    main()

