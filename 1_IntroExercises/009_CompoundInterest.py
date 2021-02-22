#!/usr/bin/env python3

INTEREST_RATE = 0.04
PERIODS = 3

try:
    P_0 = float(input('Enter your initial principal investment: '))

except ValueError as e:
    print('ERROR: Principal amount must be a number.')
    P_0 = float(input('Enter your initial principal investment: '))

balances = [P_0 * (1 + INTEREST_RATE)**i for i in range(1, PERIODS + 1)]

for i, bal in enumerate(balances):
    print(f'Year {i + 1} balance: ${bal:.2f}')
