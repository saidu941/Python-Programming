import math
import random
random= random.randint(0,9)
inputn=int(input('enter a random number'))

print(random)
print(inputn)

if inputn<random:
    print('entered number is below')
elif inputn>random:
    print('entered number is above')
else:
    print("entered number is perfect")