
unsorted = [8,4,23,42,16,15]

def insertionSort(arr):
    for idx, num in enumerate(arr):
        current_val = num
        print("current", current_val)
        i = idx-1
        print("i", i)
        while i > -1 and arr[i] > current_val:
          arr[i+1] = arr[i]
          i -= 1
        arr[i+1] = current_val
        print(arr)
    return arr
 
if __name__ == "__main__":
    print(insertionSort(unsorted))