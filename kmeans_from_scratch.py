from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import random
import math
import numpy as np


def euclidean_distance(list_1, list_2):
    return math.sqrt(sum([(list_1[i]-list_2[i])**2 for i in range(len(list_1))]))


class KMeansClustering():
    def __init__(self, nclusters):
        self.nclusters = nclusters
        self.centroids = None
    
    def train(self, dataset):
        dataset_len = len(dataset)
        dataset_observation_len = len(dataset[0])
        # Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.
        dataset = [dataset[i] for i in random.sample(list(range(dataset_len)), dataset_len)]
        init_centroids_idx = random.sample(list(range(dataset_len)), self.nclusters)
        centroids = [dataset[i] for i in init_centroids_idx]
        print(init_centroids_idx)
        prev_state = [-1] * dataset_len

        finish_cycle = False

        while not finish_cycle:
            curr_state = []
            # Compute the sum of the squared distance between data points and all centroids.
            for observation in dataset:
                centroid_min_dist = -1
                centroid_min_dist_number = -1
                for cntr in range(self.nclusters):
                    centroid_dist = euclidean_distance(observation, centroids[cntr])
                    if centroid_dist < centroid_min_dist or centroid_min_dist < 0:
                        centroid_min_dist = centroid_dist
                        centroid_min_dist_number = cntr
                # Assign each data point to the closest cluster (centroid).
                curr_state.append(centroid_min_dist_number)

            print(f'Previous state: {prev_state}')
            print(f'Current state: {curr_state}')
            # input()
            
            if curr_state == prev_state:
                # Keep iterating until there is no change to the centroids. i.e assignment of data points to clusters isn’t changing.
                finish_cycle = True
            else:
                print(f'Centroids prev: {list(np.around(np.array(centroids),2))}')
                prev_state = curr_state
                # Compute the centroids for the clusters by taking the average of the all data points that belong to each cluster.
                centroids = [[0] * dataset_observation_len for _ in range(self.nclusters)]
                cluster_count = [0 for _ in range(self.nclusters)]
                for i in range(dataset_len):
                    centroids[curr_state[i]] = [centroids[curr_state[i]][j] + dataset[i][j] for j in range(dataset_observation_len)]
                    cluster_count[curr_state[i]] += 1
                for cntr in range(self.nclusters):
                    centroids[cntr] = [centroids[cntr][j] / cluster_count[cntr] for j in range(dataset_observation_len)]
                print(f'Centroids new: {list(np.around(np.array(centroids),2))}')
        
        self.centroids = centroids






dataset = load_iris()
print(dataset.data[[10, 25, 50]])
print(dataset.target[[10, 25, 50]])
print(list(dataset.target_names))
print(len(dataset.data))

# Since clustering algorithms including kmeans use distance-based measurements to determine the similarity between data points
# it’s recommended to standardize the data to have a mean of zero and a standard deviation of one 
# since almost always the features in any dataset would have different units of measurements such as age vs income.

scaler = StandardScaler()
data_for_kmeans = scaler.fit_transform(dataset.data)

kmeans = KMeansClustering(nclusters=5)
kmeans.train(dataset.data)

print(list(np.around(np.array(kmeans.centroids),2)))

# [array([6.85, 3.08, 5.72, 2.05]), array([5.01, 3.43, 1.46, 0.25]), array([5.88, 2.74, 4.39, 1.43])]
# [array([5.01, 3.43, 1.46, 0.25]), array([6.85, 3.08, 5.72, 2.05]), array([5.88, 2.74, 4.39, 1.43])]
# [array([6.85, 3.07, 5.74, 2.07]), array([5.01, 3.43, 1.46, 0.25]), array([5.9 , 2.75, 4.39, 1.43])]


# [array([6.42, 2.92, 4.6 , 1.44]), array([7.12, 3.11, 6.03, 2.13]), array([6.2 , 2.88, 5.18, 1.93]), array([5.01, 3.43, 1.46, 0.25]), array([5.53, 2.64, 3.96, 1.23])]  
# [array([7.48, 3.12, 6.3 , 2.05]), array([6.25, 2.85, 4.78, 1.57]), array([5.53, 2.64, 3.96, 1.23]), array([6.53, 3.06, 5.51, 2.16]), array([5.01, 3.43, 1.46, 0.25])] 
# [array([5.37, 3.8 , 1.52, 0.28]), array([6.24, 2.86, 4.81, 1.62]), array([6.91, 3.1 , 5.85, 2.13]), array([5.53, 2.62, 3.94, 1.22]), array([4.82, 3.24, 1.43, 0.23])]