## 01.
a=10
b=20
if a>b:
    print("a is larger than b")
else:
    print("b is larger than a")


## 02.
a=int(input("Enter a valu for variable A:"))
if a%2==0:
    print("Even Number.")
else:
    print("Odd Number.")


## 03.
Number=int(input("Enter the Number"))
if Number>=0:
    print("This is an positive number or zero.")
else:
    print("This is a negative number.")


## 04.ফাংশন ব্যবহার করে ত্রিভূজের ক্ষেত্রফল নিণয়:-
a=int(input("Enter a value for variable A:"))
b=int(input("Enter a value for variable B:"))
c=int(input("Enter a value for variable C:"))
if(a+b)>c and (b+c)>a and (c+a)>b:
    S=(a+b+c)/2
    Area=(S*(S-a)*(S-b)*(S-c)) **0.5
    print("Area of the Triangle:",Area)
else:
    print("Triangle is not Possible.")
