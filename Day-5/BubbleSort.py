# Bubble Sort Algorithm

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# Input: N = 5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting we get 1,2,3,4,5

def bubbleSort(arr1):
    for i in range(0,len(arr1)):
        for j in range(0,(len(arr1))-i-1):
            if arr1[j] > arr1[j+1]:
                arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
    return arr1    




arr1=[5,4,3,2,1] 

print("sorted array are: ",bubbleSort(arr1))


# ✅ Bubble Sort Algorithm (Short Notes)
# Start from the first element of the array.

# Compare each pair of adjacent elements.

# If the left element is greater than the right one, swap them.

# Repeat step 2 for the entire array.

# After each full pass, the largest unsorted element moves to the end.

# Repeat the process for the remaining unsorted part, reducing the range by 1 each time.

# Stop when no swaps are needed in a full pass (optional optimization).

