try:
    from hashtable import Hashtable
except:
    from .hashtable import Hashtable

def left_join(hashmap_left, hashmap_right, join_type="left"):
    if join_type == "left":
        outer = hashmap_left
        inner = hashmap_right
    else:
        inner = hashmap_left
        outer = hashmap_right
    collection = []
    if type(outer) is dict and type(inner) is dict:
        for key in outer:
            words = []
            words.append(key)
            words.append(outer[key])
            if key in inner.keys():
                words.append(inner[key])
            else:
                words.append("NONE")
            collection.append(words)
        return collection
    for item in outer._buckets:
        if item:
            current = item
            while current:
                words = []
                words.append(current.key)
                words.append(current.value)
                if inner.contains(current.key):
                    words.append(inner.get(current.key))
                else:
                    words.append(None)
                current = current.next
                collection.append(words)
    return collection


if __name__ == "__main__":
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
    actual = left_join(hashtableS, hashtableA)
    for a in actual:
        print(a)