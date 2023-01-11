""" T-distributed Stochastic Neighbor Embedding (t-SNE)
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

def main():

    # Importing the dataset
    dataset = pd.read_csv('Wine.csv')
    X = dataset.iloc[:, 0:13].values
    y = dataset.iloc[:, 13].values

    # Feature Scaling
    sc = StandardScaler()
    X = sc.fit_transform(X)
    # Applying t-SNE
    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X, y)

    # Visualising the embeddings distribution
    x_axis = X_tsne[:, 0]
    y_axis = X_tsne[:, 1]
    
    plt.figure(figsize=(20, 8))
    sc = plt.scatter(x_axis, y_axis, c = y, alpha=.4)
    plt.title('t-SNE visualization')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.colorbar(sc)
    plt.show()

if __name__ == '__main__':
    main()