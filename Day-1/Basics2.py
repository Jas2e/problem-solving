# ● Read Integer (N) and Print the First Three Powers (N^1, N^2, N^3)
number=float(input("Enter the integer: "))

print("N^1: ",number**1,"\nN^2: ",number**2,"\nN^3: ",number**3)

# ● GCD of Two Numbers
def gcd(num1,num2):

    while num2!=0:
        rem=num1%num2
        num1=num2
        num2=rem
    return num1


n1=float(input("Enter first Number: "))
n2=float(input("Enter second  Number: "))
print("gcd of given number is: ",gcd(n1,n2))


# ● LCM of Two Numbers

def gcd(a,b) :
    while b!=0:
        a,b=b,a%b
        gcd=a
    return a 

def LCM(a,b):
    gcd1=gcd(a,b)
    lcm=(a*b)/gcd1
    return lcm

n1=float(input("Enter first Number: "))
n2=float(input("Enter second  Number: "))
print("lcm of given number is: ",LCM(n1,n2))



# ● Percentage of 5 Subjects

marks=list(map(int,input("enter the 5 subject marks: ").split()))

total=sum(marks)

Percentage=(total/500)*100

print("percentage of five subjects are: ",Percentage,"%")

# ● Converting Temperature Celsius into Fahrenheit
Celsius=float(input("enter ther temperture: "))

Fahrenheit=(Celsius*(9/5))+32

print("Temperature Celsius into Fahrenheit is: ",Fahrenheit)

