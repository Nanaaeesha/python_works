students_firstname =['aishat','uthman','korede','kayode','fathia','mumeenah']
staff_firstname =['damilare','femi','ojo','Adebodun','shola']

print("Welcome To SQI College of ICT Ogbomosho".center(100,'-'))
user = input('''
             who are you?
             1. staff
             2. student
             3. visitor


            :''')
if user.strip()=="1" or user.lower().strip()=='staff':
    first_name =input('firstname:').lower().strip()
    if first_name in staff_firstname:
        print(f'Access granted.welcome to school {first_name}')
    else:
        print('Access denied.record not found') 
  
elif  user.strip()=="2" or user.lower().strip()=='student':
    first_name =input('firstname:').lower().strip() 
    if first_name in students_firstname:
        user = input(f'''payment status
             
             1. full payment
             2. part payment
             3. no payment


            :''')
        if user.lower()=="1" or user.strip().lower()=="full payment":
                print(f'access granted.welcome to school  {first_name}')

        elif user.lower()=="2" or user.strip().lower()=="part payment":
                print(f'access granted.welcome to school {first_name}.make sure you complete your part before weekends')
                
        elif user.lower()=="3" or user.strip().lower()=="no payment":
                print(f'access denied.see the front desk and made payment {first_name}')     
                
        else:
            print("you are not our student.register now")

elif user.strip()=="2" or user.lower().strip()=='visitor':
    print('Welcome to our school.how can i help you')


      

     