#task 1

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

#task 2
    import string

    alpha = set(string.ascii_lowercase)
    input = 'qwertyuiopasdfghjklzxcvbnm'
    # print(alpha)
    # print(set(input.lower()))
    print(set(input.lower()) >= alpha)
    input = 'hjfsdfih fahsdfhika hsadjfhoafn  jfkdsf'
    print(set(input.lower()) >= alpha)




#task 3
#Python program to find the numbers which are divisible by 5 and multiple of 2

# from the range of 700-1700

x = int(input("Enter FROM number: "))
y = int(input("Enter TO number: "))

for i in range(x,y):
    if(i%5==0) and (i%2==0):
        print(i)
        print("")
