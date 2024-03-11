
var = input('your ussd code:')
if var != '*323#':
    print('invalid user code')

else:
    print('''Welcome to Mymtn
          1.Data plans
          2.social bundles
          3.Business plans
          4. borrow credit/recharge

''') 
    
user = input('option:')
if user =='1':
        print('''
             1.Daily/weekly
              2.monthly
              3.2-3month
              4.family pack
              5.hot deals


''')
elif user == '2':
     print('''
            1. whatsapp
           2.facebook
           3.instagram
           4.tiktok
           5.All social bundles

''' )      
elif user =='3':
     print('''
            1.Data coupon
           2.Broadband bundles
           3.Mifi
           4.Bizplus bundles & VAS
''')

elif user== '4':
       print('''
            1.Borrow Airtime
             2.borrow data
             3.Recharge

''' )
             
else:
      print('exit')

