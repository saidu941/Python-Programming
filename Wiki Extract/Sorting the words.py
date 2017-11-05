import string

set1=['music','film','python']

set1.sort()
len1=len(set1)
count=1
for y in set1:
    if(count==len1):
        print(y)
    else:
        print(y,end=",")
        count=count+1