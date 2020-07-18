# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    header = next(rows)
    cost = 0;

    for num, row in enumerate(rows, start=1):
        record = dict(zip(header, row))
        try:
            shares = int(record['shares'])
            value = float(record['price'])
            cost += shares * value
        except ValueError:
            print(f'Row {num}: Couldn\'t convert: {row}')
    f.close()
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

