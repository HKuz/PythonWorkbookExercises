#!/usr/bin/env python3

small_dep = 0.10
large_dep = 0.25

num_smalls = int(input('Enter the number of small (<=1 liter) bottles: '))

while num_smalls < 0:
    print('The number of bottles must be positive!')
    num_smalls = int(input('Enter the number of small (<=1 liter) bottles: '))

num_larges = int(input('Enter the number of large (>1 liter) bottles: '))

while num_larges < 0:
    print('The number of bottles must be positive!')
    num_larges = int(input('Enter the number of large (>1 liter) bottles: '))

total_refund = num_smalls * small_dep + num_larges * large_dep

print(f'Your total refund is ${total_refund:.2f}.')
