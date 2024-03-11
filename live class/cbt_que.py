exam =[('1.who is the president of nigeria\n a.)buhari b.)BAT','b'),
          ('2.how many state are in nigeria \na.)34 b.)36','a'),
         ('3.how many days makes a week\na.)5 b.)7','b'),
          ('4. what is my complexion a.)light b.)chocolate',"a"),
           ('5.i am married a.)no b.)yes','b') ]

score = 0

for question,ans in exam:
  print(question)
  user =input('answer:').strip().lower()
  if user==ans:
    print('correct')
    score +=5
  else:
    print('wrong')


print('your total score is',score) 