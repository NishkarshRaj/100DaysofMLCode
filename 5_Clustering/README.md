## Clustering Algorithms

[1. K Means Clustering](K_Means)

[2. Hierarchical Clustering](Hierarchical_Clustering)

## Pros and Cons of Clustering algorithms

![Img](img/Pros_Cons.png)

## K-Means Clustering

### Introduction
K-Means is an unsupervised machine learning algorithm. The algorithm divides the data points into k groups (called clusters), where each data point can belong to only one cluster. K-Means aims to group together similar data points into the same cluster, while keeping different clusters as far apart as possible. 

Each cluster has a center, which is a data point that represents the center of the cluster. A data point gets added to a cluster whose center is closest to that data point. Distance between points is measures using sum of squared distances method.

### Algorithm

 1. Select the number of clusters, k
 2. Appoint k data points as cluster centers (either random assignment, or space them as far apart as possible)
 3.  Until cluster assignments do not change, do the following for each data point:
	 1. Calculate the sum of squared distance between it and all the cluster centers.
	 2. Assign the point to the cluster having the closest center.
	 3. Recalculate the center for clusters by taking the average of all data points assigned to that cluster.

### Additional Information

 1. K-Means clustering is highly sensitive to the initially chosen cluster centers. Hence, K-means can be run with different starting cluster centers to get optimum results.
 2. If you do not know the optimum number of clusters to divide the data, try the algorithm with different values of k and select the best k for which the data gets nicely grouped together.

## Hierarchical Clustering - Agglomerative Clustering

Initially, each data point is treated as an independent cluster. At each step, the two closest clusters are merged to become one cluster. This process continues until only a single cluster remains. Once the process is complete, we can cut the tree into clusters as needed.