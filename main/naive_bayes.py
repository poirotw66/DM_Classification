import numpy as np
import pandas as pd

train_file = pd.read_csv('data/train_labeled.csv')
val_file = pd.read_csv('data/val_labeled.csv')

train_label = train_file.iloc[:,6:]
train_data = train_file.iloc[:,:6]

val_label = val_file.iloc[:,6:]
val_data  = val_file.iloc[:,:6]

#Categorical Naive Bayes
from sklearn.naive_bayes import CategoricalNB
clf = CategoricalNB()
clf.fit(train_data, train_label)
result_NB=clf.predict(val_data)

from sklearn.metrics import accuracy_score
score = accuracy_score(val_label, result_NB)
print('Accuracy Score: ',score*100,'%')