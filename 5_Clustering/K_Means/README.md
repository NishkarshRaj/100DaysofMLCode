# K-MEANS CLUSTERING

<strong>K-MEANS CLUSTERING</strong> is one of the simplest and popular unsupervised machine learning algorithms. <br/>
<br/>
The objective of K-means is simple: group similar data points together and discover underlying patterns. To achieve this objective, K-means looks for a fixed number (k) of clusters in a dataset.

- Step 1: Choose the number K of clusters.
- Step 2: Select at random K points, the centroids(not necessarily from your dataset)
- Step 3: Assign each data point to the closest centroid. That forms K clusters.
- Step 4: Compute and place the new centroid of each cluster.
- Step 5: Reassign each data point to the closest centroid. If any assignment took place, go to step 4, otherwise FINISH.

**RANDOM INITIALIZATION TRAP:** It is a problem that occurs in the K-Means algorithm. When the centroids of the clusters tobe generated are explicitly defined by the User the inconsistency maybe created and this may sometimes lead to generating wrong clusters in the dataset.
*Solution*: K-Means++
