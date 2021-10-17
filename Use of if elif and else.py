#Programmer Sadiq
#By@Sadiqul Islam
#Use of if else statement


#if else statement

a = int(input('Enter any number:'))

if a%2==0:
    if a%3==0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 but not by 3')

elif a%3==0:
    print('Divisible by 3 but not by 2')

else:
    print('Not divisible by either 2 or 3')
