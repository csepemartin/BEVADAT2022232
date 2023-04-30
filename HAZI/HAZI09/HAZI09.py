from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
import numpy as np
from scipy.stats import mode
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


class KMeansOnDigits():
    

    def __init__(self,n_clusters,random_state):
        self.n_clusters= n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()


    def predict(self):
        model = KMeans(n_clusters=self.n_clusters,random_state=self.random_state)
        self.clusters = model.fit_predict(self.digits.data)

    def get_labels(self):
        result = np.full_like(self.clusters,'77')
        for i in range(len(self.digits.target_names)):
            each_cluster = np.where(self.clusters==i)
            modes = mode(self.digits.target[each_cluster]).mode[0]
            result[each_cluster] = modes
        self.labels = result

    def calc_accuracy(self):
        return np.round(accuracy_score(self.digits.target,self.labels),2)
    
    def confusion_matrix(self):
        self.mat = confusion_matrix()
        
