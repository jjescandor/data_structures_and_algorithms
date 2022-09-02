try:
    from hashtable import Hashtable
except:
    from .hashtable import Hashtable

def dict_left_join(outer, inner):
    collection = []
    for key in outer:
        words = []
        words.extend([key, outer[key], inner[key] if key in inner.keys() else "NONE"])
        collection.append(words)
    return collection


def left_join(hashmap_left, hashmap_right, join_type="left"):
    outer = hashmap_left if join_type=="left" else hashmap_right
    inner = hashmap_right if join_type=="left" else hashmap_left
    collection = []
    if type(outer) is dict and type(inner) is dict:
        return dict_left_join(outer, inner)
    for key in outer.keys():
        collection.append([key,outer.get(key),inner.get(key)])
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