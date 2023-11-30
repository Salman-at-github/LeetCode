# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# O(n^2)

def findElements(nums, target):
    n = len(nums)
    # first num will be i
    for i in range(n):
        # i is added to every next(i+1) element
        for j in range(i+1,n):
            if(nums[i]+nums[j] == target):
                return [i,j]
    # if loop execution brings no result, return not found
    return "Not found"

result1 = findElements([1,2,5,6,8],  20)
# print(result1)


# O(n) : if x+y = target, then y = target - x, and if that y is in the array, that means x and y are the values we  need
def getIndices(arr, target):
    n=len(arr)
    seen = {} #store num with its index here, we will check if y exists in {},
    for i in range(n):
        diff = target - arr[i]
        if(diff in seen):   # y exists as num in array, it means we have x and found y
            return [i, seen[diff]]
        else: #if its not in {}, add number with its index to {} so that we can compare future diff to it 
            seen[arr[i]] = i    #{number : index}
    return "404 Not Found"

result2 = getIndices([1,2,4,6,9], 6)
print(result2)

# It is O(n) because we are iterating the array only once and pushing items into seen{} at the same time