import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np

'''Test för plottning'''
# X = np.array([[5,3],
# [10,15],
# [15,12],
# [24,10],
# [30,30],
# [85,70],
# [71,80],
# [60,78],
# [70,55],
# [80,91] ])
#
# from sklearn.cluster import AgglomerativeClustering
# cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
# cluster.fit_predict(X)
#
# plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')
# plt.show()

customer_data = pd.read_csv('shopping_data.csv')

customer_data.shape

customer_data.head()

#Filter columns
data = customer_data.iloc[:, 3:5].values



linked = linkage(data, 'ward')

plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.show()

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)

plt.scatter(data[:, 0], data[:, 1], c=cluster.labels_, cmap='rainbow')
plt.show()