# To check if a number is an armstrong number.


def armstrong(num):
    temp=num
    power=len(str(num))
    sum=0

    while temp!=0:
        digit=temp%10
        sum+=digit**power
        temp//=10
    if sum==num:
        return True
    else:
        return False    





number=int(input("Enter a Number:"))

print(armstrong(number))