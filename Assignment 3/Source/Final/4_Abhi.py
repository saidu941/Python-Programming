from nltk.tokenize import word_tokenize,sent_tokenize,wordpunct_tokenize

from nltk.stem import LancasterStemmer,WordNetLemmatizer

from nltk import pos_tag,ne_chunk,ngrams

from collections import Counter



f=open("input.txt","r")

content=f.read()

print("file contents\n",content)

words=word_tokenize(content)
print(words)
lem=WordNetLemmatizer()

print("\n after Lemmatization\n")

lemm_text=[]

for w in words:
    lemm_text.append(lem.lemmatize(str(w),pos="v"))
print(lemm_text)
print("after adding tags")
tag1=pos_tag(lemm_text)
print(tag1)

rem_verb=[t for t in tag1 if t[1] not in ('VB','VBN')]

print("\nAfter removing verb words\n ")

print(rem_verb)

list=[item[0] for item in rem_verb]


print("\n words count\n ",Counter(list),"\n")

repeated=Counter(list).most_common(5)
print("\nTop five common words\n",repeated)
most=[l[0] for l in repeated]
print("\n sentences having the top words \n\n")

sentences=sent_tokenize(content)

summary=""

for k in sentences:

    if any(word in k for word in most):

        print(k)

        summary=summary+k

print("\nAfter concatenating sentences\n")

print(summary)