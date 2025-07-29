# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

# Examples:

# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

# Example 2:
# Input: 6

# Output: 0 1 1 2 3 5 8
# Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)
def fibo(n):
    # if n==0 or n==1:
    #     return n
    
    # return fibo(n-1) + fibo(n-2)
    fibo=[]
    fibo[0]=0
    fibo[1]=1
    for i in range(2, n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])    

print(fibo(10))

