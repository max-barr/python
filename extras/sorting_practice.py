# arr = [2,4,6,8]
# arr[0], arr[1] = arr[1], arr[0]
# print(arr)

def bubbleSort(arr):
    for m in range(len(arr)):
        for i in range(len(arr)-1-m):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print("swapped", arr[i], "and", arr[i+1])
    return arr

arr= [6,1,67,4,5,89,3,4,1]
print(bubbleSort(arr))