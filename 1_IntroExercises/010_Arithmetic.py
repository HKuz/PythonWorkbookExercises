#!/usr/bin/env python3

import math

a = int(input('Enter integer a: '))
b = int(input('Enter integer b: '))

print(f'The sum of {a}+{b} = {a + b}')
print(f'The difference of {a}-{b} = {a - b}')
print(f'The product of {a}*{b} = {a * b}')
print(f'The quotient of {a}/{b} = {divmod(a, b)[0]}')
print(f'The remainder of {a}/{b} = {divmod(a, b)[1]}')
print(f'The log (base 10) of {a} = {math.log10(a):.3f}')
print(f'The result of {a}^{b} = {a**b}')
