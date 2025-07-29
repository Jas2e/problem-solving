# Understand recursion by print something N times
# def numtill(n):
    
#     if n==11:
#         return
#     print(n)

#     numtill(n+1)
# num=0

# print(numtill(num))

# Print 1 to N using Recursion

# def ntimes(i,num):
#     if i>num:
#         return
#     print(i)
#     ntimes(i+1,num)



# n=int(input("enter the number: "))

# ntimes(1,n)

# Print N to 1 using Recursion


def ntimes(num):
    if num <= 0:
        return
    print(num)
    ntimes(num-1)



n=int(input("enter the number: "))

ntimes(n)
