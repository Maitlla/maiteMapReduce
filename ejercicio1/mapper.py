#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    # Comprobamos si la línea tiene el formato correcto
    if len(data) != 6: 
        continue
    date, time, store, item, cost, payment = data
    print(f"{store}\t{cost}")


"""
# comprobar el código
with open("mini-purchase.txt", "r") as file:
    for line in file:
        data = line.strip().split("\t")
        if len(data) != 6:
            print(f"Error: La línea no tiene suficientes campos: {data}")
            continue
        date, time, store, item, cost, payment = data
        print(f"{store}\t{cost}")

"""
