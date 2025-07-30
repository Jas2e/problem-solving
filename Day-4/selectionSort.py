list1=[4,2,5,7,8,3,1,0]

for i in range(len(list1)):
    min_index = i

    for j in range (i+1, len(list1)):
        if list1[j] < list1[min_index]:
            min_index = j
    list1[i], list1[min_index] = list1[min_index], list1[i]
print("Sorted array:", list1)        



# write a algorithm to sort the list using selection sort.
# Start from the first index.

# Find the minimum element in the unsorted part of the array.

# Swap it with the element at the current index.

# Move to the next index and repeat until the array is sorted.
