Foods=['jollofrice','friedrice','Amala','iyan','spaggetti','yam']
drinks=['tablewater','sprite','coke','fanta','pulpy','sosa']
snacks=['fishrolls','meat-pie','sausage','croissant','sharwama']
Proteins=['friedchicken','pepperedchicken','meat','Assortedmeat','beef','fish']





print("Welcome To TREASURE HUB RESTURANT".center(100,'-'))
user = input('''
             Here is our Menu
             1. Food
             2. Drinks
             3. Snacks
             4.proteins


            :''')
if user.strip()=="1" or user.lower().strip()=='foods':
    food =input('foods:').lower().strip()
    if food in Foods:
        print(f'Available .And whatelse')
    else:
        print('not available,kindly go through our menu')

elif user.strip()=="2" or user.lower().strip()=='drinks':
    drink =input('drinks:').lower().strip()
    if drink in drinks:
        print(f'Available .And whatelse')
    else:
        print('not available,kindly go through our menu')
elif user.strip()=="3" or user.lower().strip()=='snacks':
    snacks =input('snacks:').lower().strip()
    if snacks in snacks:
        print(f'Available .And whatelse')
    else:
        print('not available,kindly go through our menu')

elif user.strip()=="4" or user.lower().strip()=='proteins':
    protein =input('drinks:').lower().strip()
    if protein in Proteins:
        print(f'Available .And whatelse')
    else:
        print('not available,kindly go through our menu')

