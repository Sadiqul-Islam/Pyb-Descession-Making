## 01.

Number=int(input("Enter the Number:"))
if Number>0:
    print("This is a positive number.")
elif Number==0:
    print("This is a zero.")
else:
    print("This is a negative number")


## 02.তিনটি নাম্বাার ইনপুট নিয়ে তাদের মধ্যে বড় নাম্বারটি বের করার প্রোগ্রাম।
a=int(input("Enter a value for variable A:"))
b=int(input("Enter a value for variable B:"))
c=int(input("Enter a value for variable C:"))
if (a>b) and (a>c):
    print("The largest number is a.")
elif (b>c) and (b>a):
    print("The largest number is b.")
else:
    print("The largest number is c.")


## 03.Grading system of general board:-
Marks=int(input("Enter Your Marks:"))
if Marks>=80:
    print("Your Grade is A+.")
elif Marks>=70:
    print("Your Grade is A. ")
elif Marks>=60:
    print("Your Grade is A-.")
elif Marks>=60:
    print("Your Grade is B+.")
elif Marks>=50:
    print("Your Grade is B.")
elif Marks>40:
    print("Your Grade is C.")
else:
    print("Your Grade is F.")


## 04.Polytechnic Grading system.
Number=int(input("Enter the Number:"))
if Number>=80:
    print("Your Grade is A+.")
elif Number>=75:
    print("Your Grade is A.")
elif Number>=70:
    print("Your Grade is A-.")
elif Number>=65:
    print("Your Grade is B+.")
elif Number>=60:
    print("Your Grade is B.")
elif Number>=55:
    print("Your Grade is B-.")
elif Number>=50:
    print("Your Grade is C+.")
elif Number>=45:
    print("Your Grade is C.")
elif Number>=40:
    print("Your Grade is D.")
else:
    print("Your Grade is F.")
    
