# pcost.py
#
# Exercise 1.27
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)

    cost = 0;
    for item in portfolio:
        cost += item['shares'] * item['price']
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

