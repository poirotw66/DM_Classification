import numpy as np
import pandas as pd

def create_data(datasize=5000,data_file='example.csv',labeldata_file='example_label.csv'):
  np.random.seed(666)
  #attitude: 0 fair, 1 good, 2 Excellent
  attitude = np.random.randint(0,3,size=datasize)
  #physical fitness: 0 fair, 1 good, 2 Excellent
  physical_fitness = np.random.randint(0,3,size=datasize)
  #technology: 0 fair, 1 good, 2 Excellent
  technology = np.random.randint(0,3,size=datasize)
  #psychological_quality: 0 glass, 1 good, 2 steel
  psych_qulity = np.random.randint(0,3,size=datasize)
  #age: 18~40
  age = np.random.randint(18,41,size=datasize)
  #potential 0~10
  potential = np.random.randint(0,11,size=datasize)
  #label 0
  label = np.zeros(datasize,int)
  dataframe = pd.DataFrame({'Attitude':attitude, 'Technology':technology, 'Potential':potential, 
                           'Age':age, 'Physical_Fitness':physical_fitness, 'Psych_Quality':psych_qulity,
                            'Label':label})
  dataframe = dataframe.reset_index()
  dataframe.to_csv(data_file,index=False,sep=',')

  train_file = pd.read_csv(data_file)

  train_data = train_file.iloc[:,1:8]


  train_data.loc[train_data['Attitude'] < 1, 'Label'] = -1             

  train_data.loc[(train_data['Attitude']>=1) & (train_data['Technology']<1) & (train_data['Potential']<5), 'Label'] = -1
  train_data.loc[(train_data['Attitude']>=1) & (train_data['Technology']<1) & (train_data['Potential']>=5 & (train_data['Age']>24)), 'Label'] = -1
  train_data.loc[(train_data['Attitude']>=1) & (train_data['Technology']<1) & (train_data['Potential']>=5 & (train_data['Age']<=24)), 'Label'] = 1

  train_data.loc[(train_data['Attitude']>=1) & (train_data['Technology']>=1) & (train_data['Physical_Fitness']>=1), 'Label'] = 1
  train_data.loc[(train_data['Attitude']>=1) & (train_data['Technology']>=1) & (train_data['Physical_Fitness']<1) & (train_data['Psych_Quality']<1), 'Label'] = -1 
  train_data.loc[(train_data['Attitude']>=1) & (train_data['Technology']>=1) & (train_data['Physical_Fitness']<1) & (train_data['Psych_Quality']>=1), 'Label'] = 1
                                                                                                                  
  train_data.head(5)
  train_data.to_csv(labeldata_file, index=False,sep=',')

create_data(50000,'train_unlabeled.csv','train_labeled.csv')
create_data(500,'val_unlabeled.csv','val_labeled.csv')