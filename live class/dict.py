# Dictionary {key:value},dict(key=value)
# print(car.get('color',not found))

# car={
#     model:'benz',
#     year:'2020',
#     color:['black','blue'],
#     owner:{
#         'name':'aishat'
#         price:7898765
#     }
# }

{
'student1':{'name':'ade','matno':202771},
'student2':{'name':'ade','matno':230574},
}

user =input('kindly press 1 to start registration:')
if user =='1':
    x=1
    student_db ={}
    while True:
        name =input('Name:').strip().title()
        matno=input('matno:').strip().title()

        students ={'name':name,'matno':matno}
        student_db.update({f'student{x}':students})


        x +=1
        user=input('press 1 to stop or enter key to continue:')
        if user == '1':
            break
        