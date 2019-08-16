import numpy as np
import pandas as pd
import scipy as sp
import mglearn as mg
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()
print('Keys of iris_dataset: \n{}'.format(iris_dataset.keys()))
print(iris_dataset['DESCR'][:193] + '\n...')
print('Target names:\n{}'.format(iris_dataset['target_names']))
print('Feature names:\n{}'.format(iris_dataset['feature_names']))
print('Type of data:\n{}'.format(type(iris_dataset['data'])))
print('Shape of data:\n{}'.format(iris_dataset['data'].shape))
print('Whole dataset:\n{}'.format(iris_dataset['data'][:]))

X_train,X_test,Y_train,Y_test = train_test_split(
	iris_dataset['data'],iris_dataset['target'],random_state=0)
print('X_train shape: {}'.format(X_train.shape))
print('Y_train shape: {}'.format(Y_train.shape))
print('X_test shape: {}'.format(X_test.shape))
print('Y_test shape: {}'.format(Y_test.shape))

iris_dataframe = pd.DataFrame(X_train,columns=iris_dataset.feature_names)
grr = pd.plotting.scatter_matrix(iris_dataframe, c=Y_train, figsize=(15,15), marker='o',
						hist_kwds={'bins':20},s=60,alpha=.8,cmap=mg.cm3)

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,Y_train)
KNeighborsClassifier(algorithm='auto',leaf_size=30,metric='minkowski',metric_params=None,
					 n_jobs=1,n_neighbors=1,p=2,weights='uniform')

Y_pred = knn.predict(X_test)
print('Test set predictions:\n {}'.format(Y_pred))
print('Test set score: {:.2f}'.format(np.mean(Y_pred == Y_test)))