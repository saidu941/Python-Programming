import matplotlib.pyplot as plt

import numpy as np

from sklearn import datasets, linear_model
from sklearn.datasets import load_boston


boston = datasets.load_boston()
boston_X = boston.data[:, np.newaxis, 2]
boston_X_train = boston_X
boston_y_train = boston.target


X,Y=boston_X_train,boston_y_train

lin_regr = linear_model.LinearRegression()
lin_regr.fit(X, Y)
plt.scatter(X, Y, color='blue')
plt.plot(X, lin_regr.predict(X), color='black', linewidth=3)
plt.show()
