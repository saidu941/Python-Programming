import string
alpha = set(string.ascii_lowercase)
input = 'qwertyuiopasdfghjklzxcvbnm'
#print(alpha)
#print(set(input.lower()))
print(set(input.lower()) >= alpha)
input = 'hjfsdfih fahsdfhika hsadjfhoafn  jfkdsf'
print(set(input.lower()) >= alpha)
