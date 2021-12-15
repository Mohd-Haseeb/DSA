def check(nums) -> bool:
    count = 0
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            count += 1
    if(nums[len(nums)-1] > nums[0]):
        count += 1
    
    return count<=1
        
arr = [4,5,6,1,5,3]
print(check(arr))