#variable decleration

# bottle = 'water'
# print(bottle)
# x=20,30
# print(x)

# x=y=z=40
# print(x)
# print(y)
# print(z)


# Value1 =int(input('first Value:'))
# Value2 = int(input('second Value:'))
# result =(Value1 + Value2)
# print(result)


# name_of_student = "yemi"
# address ="ogbomosho"
# state ="oyo"
# age ="20"
# account_bal =2000
# # print( 'my name is '+name_of_student+',i live in  '+address+'.'+ 'i am native of'+state+'i am a' +str(age)+'yearsold.')
# print(f"My name is 1{name_of_student}.I live in{address} {state}.i am {age} years old.")
# val = range(1,11,4)
# val2 = list(val)
# print(val2)


# my_dict ={'name':'aisha','course':'data science'}
# print(my_dict.items())

# my_set_num ={6,7,5,9.1,3}
# print(my_set_num)

# my_set_str ={ 'fatia','aishat','bolu',''}
# print(my_set_str)




# my_set ={2,4,5,3,6,7,8}


# Arithmetic operator
# ques = input( 'you don chop?(yes or no):')
# if ques =='yes':
#     print('do giveaway')
# elif ques == 'Yes':
# print('do giveaway 2')

# elif ques == 'YES':
# print('do giveaway 3')

# else:
# print('go and sleep')
# x=10
# if x <=10:
#     print('x is not less than ten')
# else:
#     print('x is not less than ten')



#  var = input('Your ussd code:')
#  if var != '*410#':
#      print('invalid ussd code...')

# else:
# print("""welcome
#       1.buy data
#       2.check data balance
#       """)



# de good resturant
# menu =['white rice','beans','bread','fried rice','jollof rice','meat','egg','coke','fanta','water'
# ] 
# user =input('your name')
# food =input('food')
# compliment =('comp')
# drink =('drink')

# if (food in menu) and (compliment in menu) and (drink in memu):
#     print(f'''
#           Degood resturant
#           order from{user}
#             1.{food}
#             2.{compliment}
#             3.{drink}

#     ''')
# elif food not in menu:
#     print(f'{food} not available')
# elif compliment not in menu:
#     print(f'{compliment} not available')
# elif drink not in menu:
#     print(f'{drink} not available')
# else:
#     print ('order not available') 

comment = 'god is good'
# print(comment.capitalize)

# ans = input('Are y0u happy? yes or no?:').strip().capitalize()
# if ans == 'yes':
#     print('opoorr')
# else:
#     print('do not give up')


# _split = comment.split()
''' 
Registration corner
'''
# student_list =[]
# user =int(input('how many student are taking the test:'))
# for student in range(user):
#     stud =input(f'name of student{student +1}')

# print(student_list)
# list comprehension
# numbers =[]
# for x in range(1,21):
#     numbers.append(x)

# numbers =[x for x in range(1,21)]
# print(numbers)

# user =int(input('how many students are taking the test:'))
# students_list =[input(f'name of student{student +1}:') for student in range(user)]
# print(students_list)
# calling each registered student to take the test
# print (students_lists)
# student_scores =[]
# items =['shoe','bag']
# prices =[1000,2000]
# # print(zip(items,prices))
# for x in zip(items,prices):
#     print(x)

#     # the Examination corner
#     score =

# '''' Ask the user how many student are taking the test'''

# user_number = int(input(' how many student are taking the test'))

# ''' register each student'''
# student_list =[input(f'student {x +1}:') for x in range(user_number)]
# print(student_list)
# '''call each student one after the other to take the test'''
# for each_student in student_list:
#     print(f'\n{each_student},its time for your test.\n') 

#     '''the test'''
#     questions =['1. what is my name\n a.)azeez aisha b.)azeez azeezat,'
#                 '2. am i a female\na.)yes b.)no',
#                '3. do you love me\na.)yes b.)no' ]
#     answers=['a','a','a']
#     score =0
#     for question,answer in zip(questions ,answers):
#         print(question)
#         user_ans =input('answer:').strip().lower()
#         if user_ans == answer:
#             print('correct')
#             score +=5
#             print(f'thanks for taking the test your total is {score}')
#             score_list.append(score)
#             print(student_list)
#             print(score_list)
        


'''practice'''

x=5 # x is of type int
x ="Sally" # x is now of type str=
# print(x)
# 

x = "awesome"
# print("Python is " + x)
# x = 5
# y = 10
# # print(x + y)


# x = "awesome"

# def myfunc():
#   x = "fantastic"
# #   print("Python is " + x)

# myfunc()

# # print("Python is " + x)
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)
# x = 5
# print(type(x))

# import random



# # print(random.randrange(1,10))
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# # print(a)
# a = "Hello, World!"
# # print(a[1])
# b = "Hello, World!"
# # print(b[2:5])
# b = "Hello, World!"
# # print(b[-5:-2])

# a = " Hello, World! "
# # print(a.strip()) # returns "Hello, World!"
# a = "Hello, World!"
# # print(a.upper())

# a = "Hello, World!"
# # print(a.replace("H", "J"))

# # txt = "The rain in Spain stays mainly in the plain"
# # x = "ain" in txt
# # print(x)
# # age = 36
# # txt = "My name is John, and I am {}"
# # print(txt.format(age))
# # txt = "We are the so-called \"Vikings\" from the north."
# # print(txt)

# # a = 200
# # b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")


''''tuple'''
students =('damilare','aisha','richard',"false",)


# unpacking
# (*list_student,) =students
# print(list_student)

# fruits =('banana','apple','mango')
# (fruits1,fruits2,fruits3)=fruits
# print(fruits)

# student =['mary','lola','dare']
# scores =[23,45,98]
# print(max(scores))
# index_max =scores.index(max(scores))
# print(student[index_max])

# mean_score = sum(scores)/len(scores)
# print(mean_ score)

# names =('mary','lola','dare','ayo')
# scores =[23,45,98 ,67]
# for name in names:
#     print(name)
# for name,score in zip(names,scores):
    # print(f'{name} scored {score}.')

# details = [
#         ('mary',23),
#         ('lola',45),
#         ('ayo',24),
#         ('femi',98)
#         ]
#     # print(details)
# for name,score in details:
#   print(f'{name} scored {score}.')

 




















































# ussd = input('your ussd code:')
# if ussd != '*312#':
#     print('invalid ussd code ...')
# else:
#     print(
#         """welcome
#         1. Data Plans
#         2. social plans
#         3.Business Plans
#         4.Borrow credit/recharge
#         """ )
#     user_choice = input("Enter the number corresponding to the service you want: ")

# if user_choice == "1":
#         print("""1. daily
#               2. weekly
#               3.monthly
#               4.2-3 month
#               """)
#     elif user_choice == "2":
#         print("""""
#               1.instagram plans
#               2.facebook plans
#               3.tiktok plans
#               """)
#     elif user_choice == "3":
#     print("""""
#               1.family plans
#               2.2-5 month plans
#               3.6 month plans
#               """)
        
    


# simple calculator

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero"


# operation = input("Enter operation (+, -, *, /): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))


# if operation == '+':
#     result = add(num1, num2)
# elif operation == '-':
#     result = subtract(num1, num2)
# elif operation == '*':
#     result = multiply(num1, num2)
# elif operation == '/':
#     result = divide(num1, num2)
# else:
#     result = "Invalid operation"


# print("Result: ", result)

    













# num =float(input('enter a number'))
# if num % 2 == 0:
#     print(num,'is even')
# else:
#     print(num,'is odd')

