#!/usr/bin/env python3

get_amt = input('Enter the amount to make into change: ')

# Convert to an integer to avoid floating point errors
amt = int(float(get_amt) * 100)

bank_dict = {200: 'Toonies',
             100: 'Loonies',
             25: 'Quarters',
             10: 'Dimes',
             5: 'Nickels',
             1: 'Pennies'}

change = {coin_name: 0 for coin_val, coin_name in bank_dict.items()}

for coin_amt, coin_name in sorted(bank_dict.items(), key=lambda t: t[0],
                                  reverse=True):
    # Check how many times the coin value evenly goes into amt
    num_coin = amt // coin_amt

    # Save the amount of that coin used for change to a dictionary
    change[coin_name] = num_coin

    # Update the amount
    amt -= num_coin * coin_amt

for coin, num in change.items():
    print(f'{coin}: {num:,.0f}')
