#!/usr/bin/python

import sys

pago_actual = None
maxima = 0.0

for line in sys.stdin:
    payment, venta = line.strip().split("\t")
    venta = float(venta)

    if pago_actual and pago_actual != payment:
        print(f"{pago_actual}\t{maxima}")
        pago_actual, maxima = payment, venta
    else:
        pago_actual, maxima = payment, max(maxima, venta)


if pago_actual:
    print(f"{pago_actual}\t{maxima}")