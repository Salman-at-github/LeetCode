# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# if we use pop method to remove duplicates, Time complexity will be O(n^2) because each pop will shift entire array by 1 n times, as size does not matter, we just sort the unique elements and leave the end part with whatever there is
def RemoveDuplicates(arr): #O(n)
    replaceFrom = 1 #because 0th element is always sorted since its a sorted array
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]: #if cur num != prev, it is unique, assign it to replaceFRom pointer
            arr[replaceFrom] = arr[i]
            replaceFrom += 1 #increase pointer to next num

    return replaceFrom #num of uniqiue elements
nums = [0,0,1,1,1,2,2,3,3,4]
res = RemoveDuplicates(nums)
print(res)