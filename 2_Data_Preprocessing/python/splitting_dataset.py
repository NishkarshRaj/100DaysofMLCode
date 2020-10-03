""" Data Preprocessing Template
"""

# Importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    # Importing the dataset
    dataset = pd.read_csv('../Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 3].values

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


if __name__ == '__main__':
    main()
