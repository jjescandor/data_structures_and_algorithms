try:
    from hashtable import Hashtable
except:
    from .hashtable import Hashtable

sentence1 = "apple! apple orange??? orange\n pear... pear pear, pear, orange orange"

sentence2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

sentence3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

special_ch = "!?@#$%^&*(){}[]|:;,.<>"


def first_repeated_word(sentence):
    hashtable = Hashtable()
    for ch in special_ch:
        sentence = sentence.replace(ch, "")
    temp_list = sentence.split(" ")
    temp_list = [x.replace("\n", "") for x in temp_list if x != ""]
    for word in temp_list:
        word = word.lower()
        if hashtable.contains(word):
            return word
        else:
            hashtable.set(word, 1)


def store_to_hastable(sentence):
    hashtable = Hashtable()
    for ch in special_ch:
        sentence = sentence.replace(ch, "")
    temp_list = sentence.split(" ")
    temp_list = [x.replace("\n", "") for x in temp_list if x != ""]
    for word in temp_list:
        word = word.lower()
        if hashtable.contains(word):
            value = hashtable.get(word) + 1
            hashtable.set(word, value)
        else:
            hashtable.set(word, 1)
    return hashtable


def hash_word_count(sentence):
    hashtable = store_to_hastable(sentence)
    collections = {}
    for word in hashtable._buckets:
        if word:
            current = word
            while current:
                collections[current.key] = current.value
                current = current.next
    return collections


def hash_most_frequently_used(sentence):
    hashtable = store_to_hastable(sentence)
    max = 0
    max_word = []
    for word in hashtable._buckets:
        if word:
            current = word
            while current:
                if current.value >= max:
                    max = current.value
                    max_word.append([current.key, current.value])
                current = current.next
    return [word[0] for word in max_word if word[1] == max]


if __name__ == "__main__":
    print("sentence 1", first_repeated_word(sentence1))
    print("sentence 2", first_repeated_word(sentence2))
    print("sentence 3", first_repeated_word(sentence3))
    print("Sentence 1 word count", hash_word_count(sentence1))
    print("Most used words: ", hash_most_frequently_used(sentence1))
