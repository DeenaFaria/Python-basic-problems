def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
    return arr


print(bubbleSort([23, 6, 12, 98, 45, 38, 23]))        