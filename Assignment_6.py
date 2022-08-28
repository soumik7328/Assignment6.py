#Assignment - 6 Full Stack Web Development using Python MySirG Decision Control
#1. Write a python script to check whether a given number is positive or non-positive
no=eval(input("Enter a number:-"))
if no>0:
    print("positive number")
else:
    print("non-posetive number")  

#2. Write a python script to check whether a given number is divisible by 5 or not
a=eval(input("Enter a number:-"))
if a%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")
#3. Write a python script to check whether a given number is even or odd
input1=float(input("Enter a number:-"))
if input1%2==0:
    print("Even number")
else:
    print("odd number")
#4. Write a python script to print greater between two numbers. Print number only once
#even if the numbers are the same.
input1=float(input("Enter a number:-"))
input2=float(input("Enter a number:-"))
if input1>input2:
    print(input1)
else:
    print(input2)
#5. Write a python script to print two given words in dictionary order
print("Enter two word")
a,b=input(),input()
if a<b:
    print(a,b)
if b<a:
    print("Words in dictionary order=",b,a)

#6. Write a python script to check whether a given number is a three digit number or not.
givennum=float(input("Enter a number:-"))
if givennum>99 and givennum<1000:
    print("given number is a three digit number")
else:
    print("given number is not a three digit number")

#7. Write a python script to check whether a given number is positive, negative or zero.
num=float(input("Enter a number:-"))
if num>=0:
    print("given number is positive number")
elif num<0:
    print("given number is negative number")  
else:
    print("given number is zero")  
#8. Write a python script to check whether a given quadratic equation has two real &
#distinct roots, real & equal roots or imaginary roots
import math
a=int(input("Enter values of a:"))
b=int(input("Enter values of b:"))
c=int(input("Enter values of c:"))
d=b*b-4*a*c
if d==0:
    root1=(-b)/(2*a)
    root2= root1
    print("Root are real and equal, Root1=",root1,"Root2=",root2)
elif d>0:
    root1= -(b+math.sqrt(d)) / (2*a)
    root2= -(b-math.sqrt(d)) / (2*a)
    print("Roots are real and distinct, Root1=",root1,"Root2=",root2)
else:
    print("Roots are imaginary")
#9. Write a python script to check whether a given year is a leap year or not.
year=int(input("Enter a year:-"))
if year%400==0 or (year%4==0 and year%100!=0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
#10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
a=eval(input("Enter a number:-"))
b=eval(input("Enter a number:-"))
c=eval(input("Enter a number:-"))
if a>=b>=c:
    print(a)
elif b>=a>=c:
    print(b)
else:
    print(c)
#11. Write a python script to take the month value in numeric format and display the number of days in it.
month=int(input("Enter the month value in numeric format:-"))
if month==1:
    print("the number of days in it 31")
if month==2:
    print("the number of days in it 28")    
if month==3:
    print("the number of days in it 31")
if month==4:
    print("the number of days in it 30")
if month==5:
    print("the number of days in it 31")
if month==6:
    print("the number of days in it 30")
if month==7:
    print("the number of days in it 31")
if month==8:
    print("the number of days in it 31")
if month==9:
    print("the number of days in it 30")
if month==10:
    print("the number of days in it 31")
if month==11:
    print("the number of days in it 30")
if month==12:
    print("the number of days in it 31")
#12. Write a python script to accept one complex number from the user and display the
#greater number between real part and imaginary part

import cmath
complex=eval(input("Enter a complex number="))
if complex.real>complex.imag:
    print("The greater number between real part and imaginary part:-",complex.real)
if complex.imag>complex.real:
    print("The greater number between real part and imaginary part:-",complex.imag)
