try:
    from hashtable import Hashtable
except:
    from .hashtable import Hashtable



def left_join(hashmap_left, hashmap_right):
    collection = []
    if type(hashmap_left) is dict and type(hashmap_left) is dict:
        for key in hashmap_left:
            words = []
            words.append(key)
            words.append(hashmap_left[key])
            if key in hashmap_right.keys():
                words.append(hashmap_right[key])
            else:
                words.append("NONE")
            collection.append(words)
        for a in collection:
            print(a)
        return collection
    for item in hashmap_left._buckets:
        if item:
            current = item
            while current:
                words = []
                words.append(current.key)
                words.append(current.value)
                if hashtableA.contains(current.key):
                    words.append(hashmap_right.get(current.key))
                else:
                    words.append(None)
                current = current.next
                collection.append(words)
    return collection


if __name__ == "__main__":
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    hashtableS = Hashtable(1024)
    hashtableS.set("diligent", "employed")
    hashtableS.set("fond", "enamored")
    hashtableS.set("guide", "usher")
    hashtableS.set("outfit", "garb")
    hashtableS.set("wrath", "anger")
    hashtableA = Hashtable(1024)
    hashtableA.set("diligent", "idle")
    hashtableA.set("fond", "averse")
    hashtableA.set("guide", "follow")
    hashtableA.set("flow", "jam")
    hashtableA.set("wrath", "delight")
    actual = left_join(synonyms, hashtableA)
    for a in actual:
        print(a)