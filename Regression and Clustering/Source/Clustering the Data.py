# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

height = np.array([4.0,4.1,4.1,4.3,4.3,4.5,4.3,4.6,4.7,4.8,4.9,5.0,5.0,5.1,5.2,5.6,5.6,])
weight = np.array([56,76,45,56,45,67,78,76,45,58,53,59,61,63,67,56,67])
size = np.array([0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3])
dataset = np.column_stack((height,weight,size))


# Fitting K-Means to the dataset
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(dataset)

# Visualising the clusters
plt.scatter(dataset[y_kmeans == 0, 0], dataset[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(dataset[y_kmeans == 1, 0], dataset[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(dataset[y_kmeans == 2, 0], dataset[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of tshirts')
plt.xlabel('')
plt.ylabel('')
plt.legend()
plt.show()