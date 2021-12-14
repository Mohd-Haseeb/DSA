# def moveZeroes(arr):
#     tempArr = [0]*(len(arr))
#     i = 0
#     for element in arr:
#         if element != 0:
#             tempArr[i] = element
#             i+=1
#     print(tempArr)

# arr = [0,1,0,3,12]
# moveZeroes(arr=arr)

# Optimized Answer

def moveZeroes(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j],arr[i] = arr[i],arr[j]
            j += 1
    print(arr)

a = [0,1,0,0,3,12,34,0,0,1]
moveZeroes(a)

# https://leetcode.com/problems/move-zeroes/submissions/