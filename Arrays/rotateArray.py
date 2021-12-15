def rotateArray(arr, k):
    temp = [0]*len(arr)
    for i in range(len(arr)):
        temp[(i+k)%len(arr)] = arr[i]
    
    arr = temp
    print(arr)


arr = [1,2,3,4,5,6]
rotateArray(arr,3)