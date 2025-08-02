# Find Second Smallest and Second Largest Element in an array
# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

# Example 1:
# Input: [1,2,4,7,7,5]
# Output: Second Smallest : 2
# 	Second Largest : 5
# Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2.

def SecMax(elements):
    maxx=float('-inf')
    secmaxx=float('-inf')
    for i in range(len(elements)):
        if  elements[i] > maxx:
            secmaxx=maxx
            maxx=elements[i]
            
        elif elements[i] > secmaxx and elements[i]!=maxx:
            secmaxx=elements[i]    
            
    return secmaxx      

def SecMin(elements):
    minn=float('inf')
    secminn=float('inf')
    for i in range(len(elements)):
        if  elements[i] < minn:
            secminn=minn
            minn=elements[i]
            
        elif elements[i] < secminn and elements[i]!=minn:
            secminn=elements[i]    
            
    return secminn
        

elements=[5,4,3,2,1]



print("sec Maximum Elements: ",SecMax(elements))
print("sec Minimum Elements: ",SecMin(elements))


