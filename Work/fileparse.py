# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(line, select=None, types=None, has_headers=False, delimiter=' ', silence_errors=True):
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    #with open(filename) as f:
    rows = csv.reader(line, delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for num, row in enumerate(rows, 1):
        if not row:    # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {num}: Couldn't convert {row}")
                    print(f"Row {num}: Reason {e}")
                continue
        # Make a dictionary
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
