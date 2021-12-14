def firstPosition(arr, k):
    start = 0
    end = len(arr)
    ans = -1

    while start <= end :
        mid = start + (end-start)//2

        if arr[mid] == k :
            ans = mid
            end = mid - 1
        elif k > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
        
    return ans
def lastPosition(arr, k):
    start = 0
    end = len(arr)
    ans = -1

    while start <= end :
        mid = start + (end-start)//2

        if arr[mid] == k :
            ans = mid
            start = mid + 1
        elif k > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
        
    return ans

def firstAndLastOccurence(arr,k):
    inital = firstPosition(arr,k)
    last = lastPosition(arr,k)

    return [inital,last]


arr = [3,3,3,3,3,3,3,7,9,14,19]
ans = firstAndLastOccurence(arr,2)
print(ans)



        