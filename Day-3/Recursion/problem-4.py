# Problem Statement: You are given an array. The task is to reverse the array and print it. 

# Examples:

# Example 1:
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# arr=list(map(int, input("Enter the elements of the array separated by space: ").split()))
def reverse(arr,start,end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]  # Swap the elements
    return reverse(arr, start + 1, end - 1)  # Recursive call with updated indices


arr=[]

for i in range(5):
    num=int(input("enter the number: "))
    arr.append(num)


print(arr)    
arr1=arr[::-1]
print(arr1)