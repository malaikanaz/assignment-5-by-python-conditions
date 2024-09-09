# Question no 1
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
if num%2 == 0:
    print("Number is divisible by 2")
elif num%3 ==0:
    print("Number is divisible by 3")
else:
   print ("Number is not divisible by both")


#Question no 2
# - Take the user age.
# - If the age is 18 or above:
# - Ask if they have a nationality of "Pakistani".
# -If yes, print "You are eligible to vote."
# -If no, print "Please obtain a valid ID to vote."
age=int(input("Enter your age here= "))
nationality=str(input("Enter your nationality here= "))
if nationality=="pakistani":
    print("You are eligible to vote")
    if age>=18:
        print ("You are eligible to vote")
    elif age<18:
        print("You are not eligible to vote")
else:
    print("Please obtain a valid ID to vote ")


#Question no 3
# - Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above
age=int(input("Please enter your age here= "))
if age<=12:
    print("You are a cute child")
elif age<=19:
    print("You are a teenager")
elif age<=59:
    print("You are an adult")
else :
    print("You are a senior resposible citizen")    


#Question no 4
#- Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.
 month =int(input("Please enter amonth between 1-12 here= "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
     print("This month has 31 days")
elif month==2:
    print("this month has 28 days")
else:
    print("This month has 30 days")
 #- Check if a year is a leap year or not.
year=int(input("Please enter the year here= "))
if year % 4 == 0:
    if (year % 100 == 0):
         if (year % 400 == 0):
            print("This is a leap year.")
         else:
             print("this is not a leap year")
        
       