students_db =[
    ('tolu','paid'),
    ('maimunat','half-paid'),
    ('mujeeb','not-paid')

]

staff_db =[
    ('femi','21'),
    ('yemi','02')

]

user = input('''
                welcome to sqi college of ict
             

           kindly clarify your identity
           1.staff
           2.student
           3.visitor
           4.none of the above
             
option''').strip()


if user=="1" or user.lower().strip()=="staff":
    staff_id = input('ID':).strip()
    staff_fname =input('first name:').strip().lower()


    fnames = []
    IDs =[]
    for fname,id in staff_db:
        fnames.append(fname)
        IDs.append(id)

    if staff_fname in fnames and staff_id in IDs:
        print('Access granted')
    else:
        print('Access denied')

elif user=='2' or user.lower() =='student':
    student_fname =input('first name:').strip().lower()

    student_firstnames =[]
    payment_status =[]

    for stud,status in students_db:
        student_firstnames.append(stud)
        payment_status.append(status)

        if student_fname in student_firstnames:_
        print(f'welcome{student_fname},kindly wait lets verify your payment status')


        _index = student_firstnames.index(student_fname)
        _status = payment_status[_index]
        # print(_status)

        if _status == 'paid':
            print(f'great,welcome to class{student name}')

        else:
            print(f"{student_fname},your payment status is '{_status}',kindly visit the front desk").

    else:
        print('record not found')




















