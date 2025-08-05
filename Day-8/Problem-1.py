# Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
def rotate(nums,k):
    k=k%len(nums)
    nums[:]=nums[::-1]               #reverse entire array
    nums[:k]=reversed(nums[:k])                #reverse first k 
    nums[k:]=reversed(nums[k:])               #reverse remaining n-k

    return nums





nums = [1,2,3,4,5,6,7]

k=3

print(rotate(nums,k))
