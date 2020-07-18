# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt' ) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            holding =  {
                'name'  : record['name'],
                'shares': int(record['shares']), 
                'price' : float(record['price'])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    rows = []
    for item in portfolio:
        value = prices[item['name']]
        difference = value - item['price']
        summary = (item['name'], item['shares'], value, difference)
        rows.append(summary)
    return rows


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for item in portfolio:
    total_cost += item['shares'] * item['price']

print('Total cost', total_cost)

current_value = 0.0
for item in portfolio:
    current_value += item['shares'] * prices[item['name']]

gain = current_value - total_cost

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'%10s %10s %10s %10s' % headers)
print(('---------- ') * len(headers))
for name, shares, price, change in report:
    print('{:>10s} {:>10d} {:>10} {:>10.2f}'.format(name, shares, '${:.2f}'.format(price), change))

print(f'Current value : {current_value:0.2f}')
print(f'Gain          : {gain:0.2f}')
