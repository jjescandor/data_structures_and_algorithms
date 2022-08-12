unsorted = [8,4,23,42,16,15]

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = [8, 4, 23]
        print("left", left)
        right = [42, 16, 15]
        print("right", right)
        arr = merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr

if __name__ == "__main__":
    print(merge_sort(unsorted))