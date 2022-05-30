# Selection Sort Algorithm 

def SelectionSort(arr):
    indexing_length = range(0, len(arr)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j

        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]

    return arr

print(SelectionSort([6,3,1,7,4,2]))