#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    date, time, store, item, cost, payment = data
    print(f"{item}\t{cost}")


"""
# comprobar el código
with open("mini-purchase.txt", "r") as file:
    for line in file:
        data = line.strip().split("\t")
        if len(data) != 6:
            print(f"Error: La línea no tiene suficientes campos: {data}")
            continue
        date, time, store, item, cost, payment = data
        print(f"{item}\t{cost}")

"""
