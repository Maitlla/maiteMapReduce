#!/usr/bin/python

# Obtener la venta más alta para cada tipo de pago de las registradas en todo el archivo

import sys

venta_mas_alta = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    date, time, store, item, cost, payment = data
    cost = float(cost)

    # venta más alta para el tipo de pago actual
    if payment in venta_mas_alta:
        venta_mas_alta[payment] = max(venta_mas_alta[payment], cost)
    else:
        venta_mas_alta[payment] = cost

# venta más alta por tipo de pago
for payment, maxima in venta_mas_alta.items():
    print(f"{payment}\t{maxima}")


"""
import sys
# comprobar el código
with open("mini-purchase.txt", "r") as file:
    for line in file:
        data = line.strip().split("\t")
        if len(data) != 6:
           continue
        date, time, store, item, cost, payment = data
        cost = float(cost)

        # venta más alta para el tipo de pago actual
        if payment in venta_mas_alta:
            venta_mas_alta[payment] = max(venta_mas_alta[payment], cost)
        else:
            venta_mas_alta[payment] = cost

# venta más alta por tipo de pago
for payment, maxima in venta_mas_alta.items():
    print(f"{payment}\t{maxima}")
"""
# salida print(f"{payment}\t{maxima}")
# Amex	498.32
# Visa	497.17
# Cash	499.55
# Discover	498.93
# MasterCard	496.04