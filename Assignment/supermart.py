                # TREASURE HUB HOME OF HAIR ACCESSORIES
menu_list =[
    ('water bead',1000),
    ('love bead',1400),
    ('glow in the dark',1200),
    ('royalbeads',1000),
    ('nairamarley',500),
    ("Elan shamp& condt",4000),
    ("vinoz shamp&condt",3000),
    ('scrunchies',1500),
    ('hairpins',400),
    ('soulmate cream',600),

]
print(menu_list)

order= input('''Welcome to Treasure Hub Home of Hair Accessories\n HERE IS OUR MENU;
            (water bead=1000
    love bead=1400
    glow in the dark=1200
    royalbeads=1000
    nairamarley=500
    Elan shamp& condt=4000
    vinoz shamp&condt=3000
    scrunchies=1500
    hairpins=400
    soulmate cream=600             
Kindly place your order:''').strip().title()

accessories=[]
prices =[]
orders=[]
order_prices =[]
for access,pri in menu_list:
    accessories.append(access)
    prices.append(pri)

if order in accessories:
    _index = accessories.index(order)
    status =prices[_index]  
    
    orders.append(order)
    order_prices.append(status)
    print(f'{order}is {status}')

while True:

    order2 =input('whatelse would you like to buy?\npress* to stop orders or 1 to continue:').strip()
    if order2=='*':
        break
    elif order2 !='*':
        if order2 in accessories:
          _index = accessories.index(order2)
        status =prices[_index]  
    
        orders.append(order2)
        order_prices.append(status)
    print(f'{order2}is {status}')
else:
    print('item not available')

for _ord,price in zip(orders,order_prices):
    print(f'{ord}-->{price}') 

print(f'Total: #{sum(order_prices)}\nTHANKS FOR YOUR PATRONAGE🥰😍')       


















