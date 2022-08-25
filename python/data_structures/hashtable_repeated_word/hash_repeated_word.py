sentence1 = "Once upon a time, there was a brave princess who..."

sentence2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

sentence3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'"]


def hash_repeated_word(sentence):
    wordCont = {}
    word = ""
    for ch in sentence.lower():
        if ch in alphabet:
            word += ch
        if ch == " ":
            if word in wordCont.keys():
                return word
            else:
                wordCont[word] = "first pass"
                word = ""


def hash_word_count(sentence):
    wordCount = {}
    word = ""
    for ch in sentence.lower():
        if ch in alphabet:
            word += ch
        if ch == " ":
            if word in wordCount.keys():
                wordCount[word] = wordCount[word] + 1
            else:
                wordCount[word] = 1
            word = ""
    return wordCount


def hash_most_frequently_used(sentence):
    wordCount = {}
    word = ""
    for ch in sentence.lower():
        if ch in alphabet:
            word += ch
        if ch == " ":
            if word in wordCount.keys():
                wordCount[word] = wordCount[word] + 1
            else:
                wordCount[word] = 1
            word = ""
    max = 0
    max_word = []
    for word in wordCount:
        if wordCount[word] > max:
            max = wordCount[word]
    for word in wordCount:
        if wordCount[word] == max:
            max_word.append(word)
    return max_word


if __name__ == "__main__":
    print("sentence 1", hash_repeated_word(sentence1))
    print("sentence 2", hash_repeated_word(sentence2))
    print("sentence 3", hash_repeated_word(sentence3))
    print("Sentence 1 word count", hash_word_count(sentence3))
    print("Most used words: ", hash_most_frequently_used(sentence3))
