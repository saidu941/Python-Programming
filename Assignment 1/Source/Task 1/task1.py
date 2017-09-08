fo = open('paragraphs.txt', 'r')
str = fo.read()
list = str.split()
print(list)
ln = len(list)
for i in range(ln):
    list[i] = list[i].strip(',')
    list[i] = list[i].strip('.')
for i in range(ln):
    count = 0
    for j in range(ln):
        if list[i] == list[j]:
            count = int(count+1)
    print(list[i], count)
    f = open('task1-output', 'a+')
    f.write("%s %d \n" % (list[i], count))