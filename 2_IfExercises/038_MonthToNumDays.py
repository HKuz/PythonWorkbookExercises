#!/usr/bin/env python3

long_months = ['january', 'jan', 'march', 'mar', 'may', 'july', 'jul',
               'august', 'aug', 'october', 'oct', 'december', 'dec']

short_months = ['april', 'apr', 'june', 'jun', 'september', 'sep',
                'november', 'nov']

# Get user input
month = input('Enter a month: ').lower()

if month in ['feb', 'february']:
    print(f'{month.title()} has 28 or 29 days.')
elif month in long_months:
    print(f'{month.title()} has 31 days.')
elif month in short_months:
    print(f'{month.title()} has 30 days.')
else:
    print('You entered an invalid month!')
