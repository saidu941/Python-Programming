import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import random


x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
print('x mean is : ',(sum(x)/len(x)))
print('y mean is : ',(sum(y)/len(y)))

n=len(x)
sumx=x.sum()
sumy=y.sum()
sumxy = (x * y).sum()
sumxx = (x ** 2).sum()

# slope and # intercept
slope = (sumxy - (sumx * sumy) / n) / (sumxx - (sumx * sumx) / n)
intercept = sumy/n - (slope * (sumx/n))
print('Intercept is : %f \nSlope is : %f' % (intercept, slope))


def regular_predictions(x, intercept, slope):
    return ((slope*x) + intercept)


linex = np.array([x/10. for x in range(100)])
liney = regular_predictions(linex, intercept, slope)

plt.plot(x, y,'*',linex,liney)
plt.show()


