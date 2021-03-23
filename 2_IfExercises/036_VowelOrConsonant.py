#!/usr/bin/env python3

letter = input('Enter a letter: ').lower()

while not letter.isalpha() or len(letter) != 1:
    letter = input('Invalid input! Enter a letter: ')

if letter == 'y':
    print(f'The letter {letter} is sometimes a vowel, sometimes a consonant!')
elif letter in 'aeiou':
    print(f'The letter {letter} is a vowel!')
else:
    print(f'The letter {letter} is a consonant!')
