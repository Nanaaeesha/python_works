myset ={'apple','pineapple','orange','cherry'}
print(myset)
balance =500
stake = float(input('stake:'))


while balance > 0 and balance > stake:

    guess =input('guess the chosen fruits:').strip().lower()
    chosen_fruit =myset.pop()
    myset.add(chosen_fruit)
    # print(chosen_fruit)

    if guess ==chosen_fruit:
        balance +=2 * stake
        print(f'you guessed right.\n your current balance is{balance}')
    else:
        balance -=stake
        print(f'wrong\n your current balance is {balance}')
        
    user =input('press 1 to replay or # to exit')
    if user =='#': 
        break 

    else:
            print('insufficient fund')


    print(f'your cashout balance is {balance}') 