# ● Area and Circumference of a Circle
import math
radius=int(input("ENTER THE RADIUS OF CIRCLE: "))
Area=radius**2*math.pi
Circumference=2*math.pi*radius
print("Area of circle is: ", Area)
print("Circumference of circle is: ", Circumference)


# ● Print Ascii Value of the Character
char=input("ENter character: ")
ascii=ord(char)
print("Ascii value is: ",ascii)


# ● Area of Triangle
base=int(input("ENTER THE base OF Triangle: "))
height=int(input("ENTER THE height OF Triangle: "))
Area2=0.5*base*height
print("Area of Triangle is: ", Area2)


# ● Convert a Person’s Name in Abbreviated

def Abbreviated_Name(name):
    parts = name.strip().split()

    intial=" "
    for word in parts:
        intial += word[0].upper()+'.'
    return intial    

fname=input("Enter your full name: ")

Abbreviated=Abbreviated_Name(fname)

print("Abbreviated name is: ",Abbreviated)


# ● Simple Interest
Principle_Amt=int(input("Enter Principle amount: "))
rate=float(input("Enter rate of intrest: "))
time=float(input("Enter time period "))

SI=(Principle_Amt*rate*time)/100

print("simple interest is: ",SI)

# ● Gross Salary of an Employee
basic=float(input("Enter the your basic salary: "))

if basic<=10000:
   hra=0.20*basic
   da=0.80*basic
elif basic<=20000:
     hra=0.25*basic
     da=0.90*basic
else:
    hra=0.30*basic
    da=0.95*basic

Gross_salary=basic+hra+da

print("Your gross salary is : ",Gross_salary)

# ● Factorial of a Given Number

def factorialnum(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact    



num=int(input("Enter the number: "))

factorial=factorialnum(num)

print("Factorial of number is: ",factorial)
