# ___SET _CALCULATOR_____




print('''
what operation would you like to perform?
      1.union
      2.intersection
      3.difference
      4.symmetric difference
      *exit

''')

user = input('option: ')

set1=set(input('Enter your first set:').strip())
set2=set(input('Enter your second set:').strip())


if user == '1':
    result=set1.union(set2)
    print('Answer:',result)
    
elif user=='2':
    result =set1 .intersection(set2) 
    print('Answer:',result)

elif user=='3':
    result =set1 .difference(set2)
    print('Answer:',result)

elif user=='4':
    result =set1.symmetric_difference(set2)
    print('Answer:',result)

elif user=="*":
    print('Exiting the set calculator.')



else:
    print('invalid choice.please print a command between 1 and 5.' )

    


    
