# CALCULATOR

print('''
what operation would you like to perform?
      1.Addition
      2.subtraction
      3.multiplication
      4.division
      *Exit

''')
user = input('option:')
num1=float(input('Enter your first number:'))
num2=float(input('Enter your second number:'))
if user == '1':
    result =num1 + num2
    print('Answer:',result)

elif user=='2':
    result =num1 - num2
    print('Answer:',result)

elif user=='3':
    result =num1 * num2
    print('Answer:',result)

elif user=='4':
    result =num1 / num2
    print('Answer:',result) 

elif user=='*':
    exit()

else:
    print('invalid command') 



