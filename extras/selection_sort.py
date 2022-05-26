# Selection Sort Algorithm 

def SelectionSort(arr):
    for m in range(len(arr) - 1):
        # find the minimum value of the array
        for i in range(len(arr) - 1 - m):
            if arr[i] < arr[i + 1]