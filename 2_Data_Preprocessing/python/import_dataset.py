""" Data Preprocessing Template
"""

# Importing the libraries
import pandas as pd


def main():
    # Importing the dataset
    dataset = pd.read_csv('../Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 3].values


if __name__ == '__main__':
    main()
