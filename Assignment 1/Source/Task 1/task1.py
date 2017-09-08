fo = open('paragraphs.txt', 'r')
string = fo.read()
list = string.split()
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
        """seen = set()
        for item in list:
            if item not in seen:
                f = open('frequency', 'a+')
                f.write("%s %d \n" %(list[i],count))"""
    print(list[i], count)
    f = open('task1-output', 'a+')
    f.write("%s %d \n" % (list[i], count))