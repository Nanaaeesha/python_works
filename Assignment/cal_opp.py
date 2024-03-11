class Calculator:
    def __init__(self) -> None:
        pass
    def add(self):
        num1=float(input('enter value one'))
        num2=float(input('enter value two'))
        return num1 + num2
    

    def subtract(self):
        num1=float(input('enter value one'))
        num2=float(input('enter value two'))
        return num1 - num2
    
    def multiply(self):
        num1=float(input('enter value one'))
        num2=float(input('enter value two'))
        return num1 * num2
    

    def divide(self):
        num1=float(input('enter value one'))
        num2=float(input('enter value two'))
        if num2!=0:
            return num1 / num2
             
        else:
            return"cannot divide by zero"
        
calculator=Calculator()


print('''
what operation would you like to perform?
      1.Addition
      2.subtraction
      3.multiplication
      4.division
      *Exit

''')
user=input('enter your choice (1/2/3/4):')
if user=='1':
    result=calculator.add()

elif user=='2':
    result=calculator.subtract()

elif user=='3':
    result=calculator.multiply() 

elif user=='4':
    result=calculator.divide()

else:
    result='invalid choice .choose value 1,2,3 or 4'

print('Result:',result)    




   
