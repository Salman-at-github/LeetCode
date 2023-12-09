# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeElement(arr, val): #O(n)
    # start pointer from first ele
    pointer = 0
    for num in arr:
        # if the el != num, 
        if num != val:
            arr[pointer] = num
            pointer += 1 #increase pointer by one when diff num is found
    return pointer

res = removeElement([1,2,4,4,4,5,6,4,9], 4)
print(res)