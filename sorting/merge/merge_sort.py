unsorted = [8,4,23,42,16,15]

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        merge(left, right, arr)
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
    if i < len(left):
        arr[k:] = left[i:]
    else:
        arr[k:] = right[j:]

if __name__ == "__main__":
    print(merge_sort(unsorted))