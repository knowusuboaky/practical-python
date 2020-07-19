# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv


def read_portfolio(filename):
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float], delimiter=',', has_headers=True)


def read_prices(filename):
    return dict(parse_csv(filename, types=[str,float], delimiter=','))


def make_report(portfolio, prices):
    rows = []
    for item in portfolio:
        value = prices[item['name']]
        difference = value - item['price']
        summary = (item['name'], item['shares'], value, difference)
        rows.append(summary)
    return rows


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'%10s %10s %10s %10s' % headers)
    print(('---------- ') * len(headers))
    for name, shares, price, change in report:
        print('{:>10s} {:>10d} {:>10} {:>10.2f}'.format(name, shares, '${:.2f}'.format(price), change))


def print_summary(portfolio, prices):
    total_cost = 0.0
    current_value = 0.0
    for item in portfolio:
        total_cost += item['shares'] * item['price']
        current_value += item['shares'] * prices[item['name']]

    gain = current_value - total_cost
    print(f'Total cost    : {total_cost:0.2f}')
    print(f'Current value : {current_value:0.2f}')
    print(f'Gain          : {gain:0.2f}')


def portfolio_report(portfolioFile, pricesFile):
    portfolio = read_portfolio(portfolioFile)
    prices = read_prices(pricesFile)

    report = make_report(portfolio, prices)

    print_report(report)
    print_summary(portfolio, prices)


def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
