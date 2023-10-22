# Importing libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# Ridge Regression

class RidgeRegression():

    def __init__(self, learning_rate, iterations, l2_penality):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.l2_penality = l2_penality

    # Function for model training
    def fit(self, X, Y):
        # no_of_training_examples, no_of_features
        self.m, self.n = X.shape

        # weight initialization
        self.W = np.zeros(self.n)

        self.b = 0
        self.X = X
        self.Y = Y

        # gradient descent learning

        for i in range(self.iterations):
            self.update_weights()
        return self

    # Helper function to update weights in gradient descent

    def update_weights(self):
        Y_pred = self.predict(self.X)

        # calculate gradients
        dW = (- (2 * (self.X.T).dot(self.Y - Y_pred)) +
              (2 * self.l2_penality * self.W)) / self.m
        db = - 2 * np.sum(self.Y - Y_pred) / self.m

        # update weights
        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db
        return self

    # Hypothetical function h( x )
    def predict(self, X):
        return X.dot(self.W) + self.b

def train(X,Y):
    # Splitting dataset into train and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                        test_size=1 / 3, random_state=0)
    # Model training
    model = RidgeRegression(iterations=1000,
                            learning_rate=0.01, l2_penality=1)
    model.fit(X_train, Y_train)
    return model, X_test, Y_test


def visualize(X, Y, Y_pred, col):
    # Splitting dataset into train and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                        test_size=1 / 3, random_state=0)
    fig, axs = plt.subplots(2)
    axs[0].scatter(X_train, Y_train, color='blue')
    axs[0].plot(X_train, Y_train, color='orange')
    axs[0].set_title('training')

    axs[1].scatter(X_test, Y_pred, color='blue')
    axs[1].plot(X_test, Y_pred, color='orange')
    axs[1].set_title('validation')

    for ax in axs.flat:
        ax.set(xlabel=col[0], ylabel=col[1])

    fig.tight_layout()
    #plt.savefig('output.png')
    plt.show()

# Driver code

def main():
    # Importing dataset
    df = pd.read_csv("../Salary_Data.csv")
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, 1].values
    col = df.columns
    #training the regression model
    model, X_test, Y_test = train(X, Y)

    # Prediction on test set
    Y_pred = model.predict(X_test)
    print("Predicted values ", np.round(Y_pred[:3], 2))
    print("Real values	 ", Y_test[:3])
    print("Trained W	 ", round(model.W[0], 2))
    print("Trained b	 ", round(model.b, 2))

    # Visualization on test set
    visualize(X, Y, Y_pred, col)


if __name__ == "__main__":
    main()
