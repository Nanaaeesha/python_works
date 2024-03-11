# FUNCTIONS
# function is a block of code that perform a specific task
# we have parametrize and unparametized 

# unparametized
# def addition():
#     value1=int(input('enter first number'))
#     value1=int(input('enter first number'))
#     result=value1+ value2
#     print(f' ans: {result}')
#addition()


# parametized
# def addition (value1 ,value2=10):
#     result=value1 +value2
#     print(f' ans: {result}')
# # addition(value1=int(input('enter the first value:')))
# addition(4,3)    


# we have global and local variable

# val1=12
# def addition (val3):
#     global val2
#     val2=10
#     result=val1 + val2 + val3


# name = "Abdulazeez"
# def no_me ():
#    global occupation
#    occupation='data science'
# print(f'my name is {name} and my occupation is {occupation}')
# # no_me()
 

# def describe():
#     print(f'my work is {occupation}')





def landing_page():
    global value1
    global value2

    name=input('Name')

    value1 = float(input('value1:'))
    value2 = float(input('value2:'))

    user =input(f'''
        my alata calculator.welcome{name}

    1.Addition
    2.Subtraction
    #.exit
 choose your operation:''').strip()
    
    if user=="1":
        addition()

    elif user=="2":
        subtraction ()

    elif user =='#':
        exit()   

    else:
        print('invalid input')
        landing_page()   #recursive function



def addition():
    print(f'Ans:{value1 + value2}')
    decide()

def subtraction():
    print(f'Ans:{value1 + value2}')
    decide()





def decide():
        user =input('press 1 to go home or enter to exit').strip
        if user == 1:
            landing_page()
        else:
            exit()    

# landing_page()
            


            #RETURN

def add (val1:float,val2:float=10):
    '''
    i add thing up
    ''' 
    return val1+val2
    #20
# print(add((10)) )

def arithmetic():
    res =2 ** add(10)
    return res

def printf(name):
    print(f'{name},your result is {arithmetic()}')

    printf(input('your name'))






    


