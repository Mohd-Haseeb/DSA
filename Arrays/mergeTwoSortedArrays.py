def merge(nums1,m,nums2,n):
    i=j=k=0
    nums3 = [0]*(m+n)
    while(i<m and (j<n)):
        if nums1[i]<nums2[j]:
            nums3[k] = nums1[i]
            k += 1
            i += 1
        else:
            nums3[k] = nums2[j]
            k += 1
            j += 1
    while(i<m):
        nums3[k] = nums1[i]
        k += 1
        i += 1
    while(j<n):
        nums3[k] = nums2[j]
        k += 1
        j += 1
    temp = 0
    for element in nums3:
        nums1[temp] = element
        temp += 1
    # print(nums1)
    print(nums1)


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,3,nums2,3)

# https://leetcode.com/problems/merge-sorted-array/submissions/