import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')



import re
def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())

from nltk import word_tokenize,sent_tokenize,wordpunct_tokenize
WORDS = tokens(file('input.txt').read())
words1=open('input.txt').read()
#print(WORDS)



#LEMMATIZATION
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lem_text=[]
for WORD in WORDS:
    y=lemmatizer.lemmatize(WORD,pos='v')
    #lem_text.append(WORD)
    lem_text.append(y)
print(lem_text)



#POS
#REMOVING ALL THE VERBS IN A TEXT FILE
from collections import Counter

remaining=[]
from nltk.tag import pos_tag
sent=(pos_tag(WORDS))
print([s for s in sent if s[1] != 'VBG'])





#WORD FREQUENCY
word_freq=[]
for WORD in WORDS:
    word_freq.append(WORDS.count(WORD))
word_counts= Counter(WORDS)
print(word_counts)
mostcommon2=word_counts.most_common(5)
print(mostcommon2)

finalmc=[]
for i in range(len(mostcommon2)):
    finalmc.append(mostcommon2[i][0])
print '\nfinal list is: ',finalmc



#Finding most repeated sentences
sentence= nltk.sent_tokenize(words1)

#finding sentences with most common words
print len(sentence)

list = []
for i in range(len(sentence)):
    splitted = word_tokenize(sentence[i])
    for j in range(len(finalmc)):
        for k in range(len(splitted)):
            if finalmc[j] == splitted[k]:
                if sentence[i] not in list:
                    list.append(sentence[i])

print 'printing list containg sentences that has most repeated words'
print list
print ' '.join(h for h in list)




