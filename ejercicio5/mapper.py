#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    date, time, store, item, cost, payment = data
    cost = float(cost)

    # para que el reducer.py sume la venta
    print(f"total\t{cost}")