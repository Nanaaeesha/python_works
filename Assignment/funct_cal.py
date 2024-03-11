# CALCULATOR USING FUNCTION

print('''
what operation would you like to perform?
      1.Addition
      2.subtraction
      3.Multiplication
      4.Division
      5.Modulus

''')
user = input('option')
# num1=int(input('Enter your first number:'))
# num2=int(input('Enter your second number:'))



if user =='1':
    def Addition():
        val1=int(input('value1:').strip())
        val2=int(input('value2:').strip())
        Result =val1+val2
        print(f"{val1}+{val2}={Result}")
    Addition()

elif user =='2':

    def Subtraction():
        val1=int(input('value1:').strip())
        val2=int(input('value2:').strip())
        Result =val1-val2
        print(f"{val1}-{val2}={Result}")
    Subtraction()

elif user =='3':

    def Multiplication():
        val1=int(input('value1:').strip())
        val2=int(input('value2:').strip())
        Result =val1*val2
        print(f"{val1}*{val2}={Result}")
    Multiplication()

elif user =='4':

    def Division():
        val1=int(input('value1:').strip())
        val2=int(input('value2:').strip())
        Result =val1/val2
        print(f"{val1}/{val2}={Result}")
    Division()

elif user =='5':

    def Modulus():
        val1=int(input('value1:').strip())
        val2=int(input('value2:').strip())
        Result =val1%val2
        print(f"{val1}%{val2}={Result}")
        Modulus()


else:
    print('invalid input')    