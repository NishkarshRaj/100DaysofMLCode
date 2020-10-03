# HIERARCHICAL CLUSTERING
There are two types of hierarchical clustering:
- Agglomerative
- Divisive

Here, we look at **Agglomerative Hierarchical Clustering**

It includes the following algorithm:
- Step 1: Make each data point a single point cluster. This forms N clusters where N is the total number of points.
- Step 2: Take the two closest data points and make them one cluster. This forms N-1 clusters.
- Step 3: Take the two closesr clusters and make them one cluster. This forms N-2 clusters.
- Step 4: Repeat step 3 until there is only one cluster.
- FINISH

How to choose the ideal number of clusters: Using **Dendogram**

```
import scipy.cluster.hierarchy as sch   #importing cluster.hierarchy from scipy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))  #using dendogram function and inputting linkage function as its argument. Method ward is used for minimizing variance inside clusters
plt.title('Dendrogram') #Naming Title of graph
plt.xlabel('Customers') #Naming entity being represented on x axis
plt.ylabel('Euclidean distances') #Naming entity being represented on y axis
plt.show()
```
This generates a dendogram. Choose the highest vertical line that doesn't cross any horizontal line(extended) and imagine a threshold line through it. The number of clusters below the threshold are considered to be the ideal number of clusters for the given dataset.
