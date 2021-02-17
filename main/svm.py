import numpy as np
import pandas as pd

train_file = pd.read_csv('data/train_labeled.csv')
val_file = pd.read_csv('data/val_labeled.csv')

train_label = train_file.iloc[:,6:]
train_data = train_file.iloc[:,:6]

val_label = val_file.iloc[:,6:]
val_data  = val_file.iloc[:,:6]

#svm
from sklearn.svm import SVC    #1. choose "Support vector claaifier"
model = SVC(kernel='rbf', gamma=0.001, C=1)  # 2. instantiate model            
model.fit(train_data, train_label)    # 3. fit model to data                                                         
result = model.predict(val_data)        # 4. predict on new data

from sklearn.metrics import accuracy_score
score = accuracy_score(val_label, result)
print('Accuracy Score: ',score*100,'%') 


# Validation Curve
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

param_range = np.logspace(-6, -1, 5)
print(param_range)
train_scores, test_scores = validation_curve(
    SVC(), train_data, train_label, param_name="gamma", param_range=param_range,
    scoring="accuracy", n_jobs=1)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.title("Validation Curve with SVM")
plt.xlabel(r"$\gamma$")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
lw = 2
plt.semilogx(param_range, train_scores_mean, label="Training score",
             color="darkorange", lw=lw)
plt.fill_between(param_range, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.2,
                 color="darkorange", lw=lw)
plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
             color="navy", lw=lw)
plt.fill_between(param_range, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.2,
                 color="navy", lw=lw)
plt.legend(loc="best")
plt.show()


model = SVC(kernel='rbf', gamma=0.1, C=100)  # 2. instantiate model            
model.fit(train_data, train_label)    # 3. fit model to data                                                       
result = model.predict(val_data)        # 4. predict on new data

from sklearn.metrics import accuracy_score
score = accuracy_score(val_label, result)
print(score) 