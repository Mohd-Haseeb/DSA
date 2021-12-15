def sumOfArrays(arr1,n,arr2,m):
    i=n-1
    j= m-1
    temp = []
    carry = 0
 
    while(i>=0 and j>=0):
        sum = arr1[i]+arr2[j]+carry
        carry = sum//10
        sum = sum % 10
        temp.append(sum)
        i -= 1
        j -= 1

    # If arr1 is longer than arr2
    while(i>=0):
        sum = arr1[i]+carry
        carry = sum//10
        sum = sum % 10
        temp.append(sum)
        i -= 1
    # If arr2 is longer than arr1
    while(j>=0):
        sum = arr1[j]+carry
        carry = sum//10
        sum = sum % 10
        temp.append(sum)
        j -= 1
    # If carry is generated at the end
    while(carry != 0):
        sum = carry
        carry = sum//10
        sum = sum%10
        temp.append(sum)

    print(temp[::-1])


arr1 = [1,2,3,4]
n = len(arr1)
arr2 = [6]
m= len(arr2)

sumOfArrays(arr1,n,arr2,m)
        

    
#https://www.codingninjas.com/codestudio/problems/sum-of-two-arrays_893186?utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_4