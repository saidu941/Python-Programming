
import pandas

import pylab as pl

from sklearn.cluster import KMeans

from sklearn.decomposition import PCA




variables = pandas.read_csv('Local_Weather_Data.csv')
Y = variables[['TempOut']]
X = variables[['HiTemp']]


#Elbow Method to find the best Number of CLusters
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
score
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()


pca=PCA(n_components=1).fit(Y)
pca_d = pca.transform(Y)
pca_c = pca.transform(X)



kmeans=KMeans(n_clusters=5)
kmeansoutput=kmeans.fit(Y)
kmeansoutput
pl.figure('5 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('5 Cluster K-Means')
pl.show()


#References
#http://www.datasciencecentral.com/profiles/blogs/python-implementing-a-k-means-algorithm-with-sklearn
