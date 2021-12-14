def peakIndexInMountainArray(arr):
        
        start = 0
        end = len(arr)-1

        while(start <= end):

            mid = start + (end-start)//2
            if (arr[mid] > arr[mid-1]) and (arr[mid] > arr[mid+1]) :
                return mid
            elif (arr[mid] > arr[mid-1] and (arr[mid] < arr[mid+1])):
                start = mid+1
            elif (arr[mid] < arr[mid-1] and (arr[mid] > arr[mid+1])):
                end = mid-1
        return -1


arr = [0,2,1,0]
res = peakIndexInMountainArray(arr)

print(res)

# https://leetcode.com/problems/peak-index-in-a-mountain-array/