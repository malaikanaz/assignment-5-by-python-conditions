# Question no 4
#Using conditional statements, check if the number is:
#- Even or Odd.
 #- Positive, Negative, or Zero.
 #- Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.
num=int(input("Enter a number here= "))
if num%2==0:
    print("Number is even")
elif num%2!=0:
    print("Number is odd")
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("Number is zero")
