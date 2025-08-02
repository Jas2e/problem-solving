# Find the Largest element in an array

# Problem Statement: Given an array, we have to find the largest element in the array.

# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the largest element in the array. 

# Example2: 
# Input: arr[] = {8,10,5,7,9};
# Output: 10
# Explanation: 10 is the largest element in the array.


def Maxele(elements):
    for i in range(0,len(elements)):
        maximum=elements[0]
        
        if  maximum < elements[i]:
            maximum=elements[i]
            
    return maximum      
        

elements=[5,4,3,2,1]

# print(max(elements))

print("Maximum Elements: ",Maxele(elements))
