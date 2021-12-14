def reverseArray(arr, p):
    start = p+1
    end = len(arr)-1
    while(start<=end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    
    print(arr)


a = [2,4,77,12,1]
reverseArray(a,1)   