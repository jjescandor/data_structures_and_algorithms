
unsorted = [8,4,23,42,16,15]

def insertionSort(arr):
    for idx in range(1, len(arr)):
        print(idx)
        i = idx-1
        current_val = arr[idx]
        while i >= 0 and current_val < arr[i]:
          arr[i+1] = arr[i]
          i = i- 1
        arr[i+1] = current_val
    return arr
 
if __name__ == "__main__":
    print(insertionSort(unsorted))