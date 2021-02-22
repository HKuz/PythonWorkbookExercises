#!/usr/bin/env python3

n = float(input('Enter a positive integer: '))

while (n != int(n) or (n < 0)):
    n = float(input('Enter a positive integer: '))

sum_n_pos_ints = (n * (n + 1)) / 2

print(f'The sum of the first {n:.0f} positive integers is: '
      f'{sum_n_pos_ints:.0f}')
