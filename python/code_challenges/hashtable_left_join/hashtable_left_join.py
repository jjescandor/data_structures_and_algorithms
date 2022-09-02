try:
    from hashtable import Hashtable
except:
    from .hashtable import Hashtable

def dict_left_join(outer, inner):
    return [[key, outer[key], inner[key] if key in inner.keys() else None] for key in outer]


def left_join(hashmap_left, hashmap_right, join_type="left"):
    outer = hashmap_left if join_type=="left" else hashmap_right
    inner = hashmap_right if join_type=="left" else hashmap_left
    return dict_left_join(outer, inner) if type(outer) is dict and type(inner) is dict else [[key,outer.get(key),inner.get(key)]for key in outer.keys()]


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