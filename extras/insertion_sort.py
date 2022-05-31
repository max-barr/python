def InsertionSort(arr):

    indexing_length = range(1, len(arr))

    # The first item in the unsorted list is the first item in the sorted list. example: 1 | 4,5,6,74,
    for i in indexing_length:
        value_to_sort = arr[i]

        # Is the value to the left higher than the value we are trying to sort? Also, i must be greater than zero because python allows negative indexing. We don't want to pull from the last value in the unsorted sublist.
        while arr[i-1] > value_to_sort and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1

    return arr

print(InsertionSort([2,3,4,5,5,5,33,4,6,756,43]))
print(InsertionSort([10,9,8,7,6,5,4,3,3,2,2,2,2,2,21,1,1,1,1]))