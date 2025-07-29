# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

# Examples:

# Example 1:
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Example 2:
# Input: N=6
# Output: 21
def summ(num):
    if  num==0:
        return 0
    
    return num + summ(num - 1)
    
    



n=int(input("enter the number: "))

print(summ(n))