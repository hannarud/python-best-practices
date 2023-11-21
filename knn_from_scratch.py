from sklearn.datasets import load_iris
import pandas as pd
import math

class KNNClassifier():
    def __init__(self, nneighbours=3) -> None:
        self.nneighbours = nneighbours
        self.data = None
        self.labels = None

    def train(self, train_features, train_target):
        self.data = train_features
        self.labels = train_target

    def predict(self, test_data, distance_func):
        if self.data is None:
            raise ValueError("Please, train the model with data first!")
        predictions = []
        # We need to save classes too!
        for test_data_example in test_data:
            dists_to_nn = []
            for i in range(len(self.labels)):
                train_data_example = self.data[i]
                train_data_label = self.labels[i]
                dist_to_this_neighbour = distance_func(test_data_example, train_data_example)
                dists_to_nn.append( (dist_to_this_neighbour, train_data_label) )
                dists_to_nn.sort(key=lambda tup: tup[0])
            neighbours = dists_to_nn[:self.nneighbours]
            output_values = [neighbour[1] for neighbour in neighbours]
            # Find majoritary class and return it as an output
            prediction = max(set(output_values), key=output_values.count)
            predictions.append(prediction)
        return predictions
            


def euclidean_distance(list_1, list_2):
    return math.sqrt(sum([(list_1[i]-list_2[i])**2 for i in range(len(list_1))]))


dataset = load_iris()
print(dataset.data[[10, 25, 50]])
print(dataset.target[[10, 25, 50]])
print(list(dataset.target_names))

classifier = KNNClassifier(nneighbours=2)
classifier.train(dataset.data, dataset.target)

labels_predicted = classifier.predict(dataset.data, euclidean_distance)

print(dataset.target)
print(labels_predicted)

df = pd.DataFrame({'target': dataset.target, 'predicted': labels_predicted})

tab = df.groupby(['target', 'predicted']).size()

print(tab)
