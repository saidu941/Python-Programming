#This program is about removing the duplicates in a given sentence and
#sorting it alphanumerically

sentence1=input('enter the sentence here: ')
print(sentence1)

words=sentence1.split()
print(len(words))

print (" ".join(sorted(list(set(words)))))