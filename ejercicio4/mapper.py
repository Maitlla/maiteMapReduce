#!/usr/bin/python

import sys

maxima_absoluta = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    date, time, store, item, cost, payment = data
    cost = float(cost)

    # venta más alta absoluta
    maxima_absoluta = max(maxima_absoluta, cost)

# Tipo de pago que tiene la venta máxima absoluta de todas las ventas registradas
print(f"{payment}\t{maxima_absoluta}")


"""
# comprobar el código
maxima_absoluta = 0.0

with open("mini-purchase.txt", "r") as file:
    for line in file:
        data = line.strip().split("\t")
        if len(data) != 6:
            continue
        date, time, store, item, cost, payment = data
        cost = float(cost)

        # Actualizamos la venta más alta absoluta
        maxima_absoluta = max(maxima_absoluta, cost)

# Imprimimos el resultado del máximo absoluto
print(f"{payment}\t{maxima_absoluta}")
"""

# salida print(f"{payment}\t{maxima_absoluta}")
# Cash	499.55

