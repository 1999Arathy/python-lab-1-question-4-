#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

user_number = int(input('enter a number'))
x=1

while(x <= user_number):
    if(user_number%x==0):
        print(x)
    x=x+1

