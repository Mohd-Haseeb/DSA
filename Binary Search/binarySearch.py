class BinarySearch:
    def binary(self,arr,key):
        start = 0
        end = len(arr)

        while(start <= end):

            mid = start + (end-start)//2

            if(arr[mid] == key):
                return mid
            
            if key > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1

bs = BinarySearch()
arr = [2,5,7,9,10,14,18,35,58]
res = bs.binary(arr,15)
print(res)

# Time Complexity -> O(logN) and Space Complexit -> O(1)