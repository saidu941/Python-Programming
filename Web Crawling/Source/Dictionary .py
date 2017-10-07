""
Use a list which contains three dictionaries. For example [{},{},{}]. Then sum the values of the dictionaries if they are integer.

[{'course': python, 'LastGPA' : 90, 'CurrentGPA': 80},{'course': python, 'LastGPA' : 95, 'CurrentGPA': 85},{'course': python,'LastGPA' : 100,'CurrentGPA': 100}]And the output like this: notice that one element has been deleted, and the new element is the join of them, the number in the new list is the average of the old numbers.[{'course': python, 'LastGPA+CurrentGPA': 85},{'course': python, ' LastGPA+CurrentGPA' : 90},{'course': python, ' LastGPA+CurrentGPA' : 100}]You can use a for loop to iterate through the list, then in each iteration, delete the item you don’t want using pop,keeping its value in a variable like n1, again deleting the item you do not want, and keeping its value in a variable like n2. Finally get the average of the vaues in n1 and n2, assign that to new item in the list like: d[‘lastGPAandCurrentGPA’]=85
""



#Dictionary and list combination
list=[]

while(0==0):
 inp = input('Enter Y to input N to exit')
 if inp.__eq__('N'):
     break
 else:
  dict1 = {}
  course = input('please enter the course name')
  lastgpa = int(input('please enter last gpa'))
  currentgpa = int(input('please enter current gpa'))
  dict1['course']=course
  dict1['lastgpa']=lastgpa
  dict1['currentgpa'] = currentgpa
  list.append(dict1)
result=[]

for value in list:
    dict2 = {}
    dict2['course'] = value['course']
    dict2['lastgpa+currentgpa']=(value['lastgpa']+value['currentgpa'])/2
    result.append(dict2)

for value in result:
    print(value)