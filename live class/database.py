import mysql.connector as sql

mycon = sql.connect(host='127.0.0.1',user = 'root',password='',database ='bank2_db')
mycursor = mycon.cursor()
mycon.autocommit = True

# # mycursor.execute('CREATE DATABASE bank2_db')
# # mycursor.execute('SHOW DATABASES')
# # print(mycursor)
# # for db in mycursor:
#     # print(db)


# mycursor.execute(
#     'CREATE TABLE customer_table(id INT(4)PRIMARY KEY AUTO_INCREMENT,fullname VARCHAR(25),email VARCHAR(25) UNIQUE,account_no VARCHAR(11) UNIQUE,account_bal FLOAT(10),date_created DATETIME DEFAULT CURRENT_TIMESTAMP)'
# )

# # mycursor.execute('SHOW TABLES')
# # for table in mycursor:
# #     print(table)

# mycursor.execute('ALTER TABLE customer_table change id customer_id INT(4) AUTO_INCREMENT')
# mycursor.execute('ALTER TABLE customer_table ADD password VARCHAR(25)')


fullname = input('fullname:')
email = input('Email:')
account_no =input('account_no:')
account_bal=input('account_bal:')
password= input('password:')

query='INSERT INTO customer_table(fullname,email,account_bal,password)VALUES(%s,%s,%s,%s,%s)'
values = (fullname,email,account_no,account_bal,password)

mycursor.execute(query,values)
print(mycursor.rowcount,'customer added successfully')
mycon.commit()




import pwinput as pw


# mycursor.execute('SELECT*FROM customer_table')
# details = mycursor.fetchall()
# print(details)

# mycursor.execute('SELECT fullname,account_no,account_bal FROM customer_table')
# details = mycursor.fetchall()
# print(details)



# mycursor.execute('SELECT  fullname,account_no,account_bal FROM customer_table WHERE customer_id = 1')
# details = mycursor.fetchall()
# print(details)


# def sigin():
#     email = input('email:').strip()
#     password =pw.pwinput()


# query = 'SELECT fullname,account_no,account_bal FROM customer_table WHERE email = % AND password =%'
# value