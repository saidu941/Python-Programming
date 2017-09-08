#Python program to find the numbers which are divisible by 5 and multiple of 2

# from the range of 700-1700

x = int(input("Enter FROM number: "))
y = int(input("Enter TO number: "))

for i in range(x,y):
    if(i%5==0) and (i%2==0):
        print(i)
        print("")
