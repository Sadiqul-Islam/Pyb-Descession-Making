## 01.
Age=int(input("Please Enter Your Age Here:"))
if Age<0:
    print("You have not borned yet!")
if Age>0 and Age<=12:
    print("You are a Child")
if Age>12 and Age<=19:
    print("You are a Teenager")
if Age>19 and Age<=40:
    print("You are a Young One!")
if Age>40:
    print("Wish you a long Life")


## 02.
a=int(input("Enter a value for variable A:"))
b=int(input("Enter a value for variable B:"))
c=int(input("Enter a value for variable C:"))
if (a>b) and (a>c):
    print("Largest Number is a.")
if (b>c) and (b>a):
    print("Largest Number is b.")
else:
    print("Largest Number is c.")
