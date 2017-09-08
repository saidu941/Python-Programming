file = open('The Beast.txt', 'r')
book = file.read()

print(book)

def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None


def count_word(tokens, token):
    count = 0
    for element in tokens:
        # Remove Punctuation
        word = element.replace(",", "")
        word = word.replace(".", "")

        # Found Word
        if word == token:
            count += 1
    return count


# Tokenize the Book
words = tokenize()

# Get Word Count
word = 'the'
frequency = count_word(words, word)
print('Word: [' + word + '] Frequency: ' + str(frequency))