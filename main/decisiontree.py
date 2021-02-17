import numpy as np
import pandas as pd

train_file = pd.read_csv('data/train_labeled.csv')
val_file = pd.read_csv('data/val_labeled.csv')

train_label = train_file.iloc[:,6:]
train_data = train_file.iloc[:,:6]

val_label = val_file.iloc[:,6:]
val_data  = val_file.iloc[:,:6]

from sklearn import tree 
import matplotlib.pyplot as plt
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data,train_label)

feature=['Attitude','Technology','Potential','Age','Physical_Fitness', 'Psych_Quality']
draft=['undrafted','picks']
plt.figure(figsize=(18,20))
tree.plot_tree(clf,feature_names=feature,class_names=draft)

result = clf.predict(val_data)        # 4. predict on new data

from sklearn.metrics import accuracy_score
score = accuracy_score(val_label, result)
print('Accuracy Score: ',score*100,'%') 

result = tree.export_text(clf,feature_names=feature)
print(result)