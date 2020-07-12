# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = int(input('Enter extra payment start month: '))
extra_payment_end_month =  int(input ('Enter extra payment end month: '))
extra_payment = float(input('Extra payment: '))
month = 0

while principal > 0:
    month = month + 1;
    if principal <= payment:
        total_paid = total_paid + principal
        principal = 0;
    if not (principal <= payment):
        if (month >= extra_payment_start_month and month <= extra_payment_end_month):
            principal = principal * (1+rate/12) - (payment+extra_payment)
            total_paid = total_paid + (payment+extra_payment)
        if not (month >= extra_payment_start_month and month <= extra_payment_end_month):
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
    print(f'{month} {total_paid:0.2f} {principal:0.2f}')
print(f'Total paid: {total_paid:0.2f}')
print(f'Month     : {month}')
