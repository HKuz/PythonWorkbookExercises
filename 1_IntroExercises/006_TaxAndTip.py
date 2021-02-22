#!/usr/bin/env python 3

TAX_RATE = .06
TIP_RATE = 0.18

food_amt = float(input('Enter the cost of food ($): '))
tax_amt = food_amt * TAX_RATE
tip_amt = food_amt * TIP_RATE
total = sum([food_amt, tax_amt, tip_amt])

print(f"""
Your Receipt:

Food: ${food_amt:.2f}
Tax ({TAX_RATE*100:.1f}%): ${tax_amt:.2f}
Tip ({TIP_RATE*100:.1f}%): ${tip_amt:.2f}
TOTAL: ${total:.2f}
""")
