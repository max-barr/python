# Selection Sort Algorithm 

def SelectionSort(arr):
    indexing_length = range(0, len(arr)-1)
    
    # Set the min value to i
    for i in indexing_length:
        min_value = i
        # iterate through everything to the right of i. If j is less than min_value, j becomes the min_value.
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        # Swapping positions
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]

    return arr

print(SelectionSort([99,3,67,4,5,1,888,345]))