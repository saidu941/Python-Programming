import numpy as np
vector1=np.random.rand(15)
print('generated vector is: ',vector1)
print('maximum value is: ',max(vector1))

#chaning it to the desired maximum value
n1=int(input('enter a value to replace the maximum value'))
vector1[vector1.argmax()]=100
print('modified vector is: ',vector1)


