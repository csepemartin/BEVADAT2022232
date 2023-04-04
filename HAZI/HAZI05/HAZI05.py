import numpy as np
import seaborn as sns
import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier:

    def __init__(self,k:int,test_split_ratio:float):
        self.k = k
        self.test_split_ratio= test_split_ratio

    @property
    def k_neighbors(self):
        return self.k
    
    @staticmethod
    def load_csv(csv_path:str):
        dataset = pd.read_csv(csv_path)
        dataset = dataset.sample(random_state=42,frac=1)
        x,y = dataset.iloc[:,:-1],dataset.iloc[:,-1]
        return x,y
    

    def train_test_split(self,features,labels):
        
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        x_train,y_train = features.iloc[:train_size,:],labels.iloc[:train_size]
        x_test,y_test = features.iloc[train_size:train_size+test_size,:], labels.iloc[train_size:train_size + test_size]
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
    

    def euclidean(self,element_of_x):
        m = element_of_x.mean()
        copypoints = self.x_train.copy()
        copypoints.loc[:,m.index] -= m
        return ((copypoints**2).sum(axis = 1))**(1/2)
    

    def predict(self,x_test:pd.DataFrame) -> pd.DataFrame:
        labels_pred = []
        for index,row in x_test.iterrows():
            one_row = row.to_frame().transpose()
            distances = self.euclidean(one_row).to_frame()
            distances['Outcome'] = self.y_train
            distances.sort_values(by=[0], inplace=True)
            label_pred = mode(distances.head(self.k),keepdims=False).mode
            labels_pred.append(label_pred[1])
            self.y_preds = pd.DataFrame(labels_pred)
        return self.y_preds
    
    def accuracy(self) -> float:
        true_positive = self.y_test.to_frame().where(self.y_test.to_frame().values==self.y_preds.values).notna().sum()
        return (true_positive / len(self.y_test) * 100)[0]
    
    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix
    

    def best_k(self):
        result = tuple()
        self.k = 1
        self.predict(self.x_test)
        max_acc = self.accuracy()
        result = (max_acc,1)
        for i in range(2,21):
            self.k = i
            self.predict(self.x_test)
            acc = self.accuracy()
            if(acc > max_acc):
                max_acc = acc
                result =(max_acc,i)
        return result
