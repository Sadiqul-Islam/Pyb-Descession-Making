#Programmer sadiq
#By@Sadiqul Islam
#Use of nested elif statement


#nested elif

x = int(input('Enter any time:' ))

if x<10:
    print('Good Morning!')

elif x<12:
    print('Soon time for lunch!')

elif x<18:
    print('Good Day!')

elif x<22:
    print('Good Evening!')

else:
    print('Good Night!')



#Example 2

marks = 78

if marks>= 80:
    print('A+')
elif marks>= 75:
    print('A')
elif marks>= 70:
    print('A-')
elif marks>= 65:
    print('B+')
elif marks>= 60:
    print('B')
elif marks>= 55:
    print('B-')
elif marks>= 50:
    print('C+')
elif marks>= 45:
    print('C')
elif marks>= 40:
    print('D+')
elif marks>= 33:
    print('D')
else:
    print('Fail')
