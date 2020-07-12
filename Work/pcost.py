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

    for row in rows:
        try:
            shares = int(row[1])
            value = float(row[2])
            cost += shares * value
        except ValueError:
             print('Bad row encountered', row)
    f.close()
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

