#!/usr/bin/python

import sys

total_ventas = 0.0

for line in sys.stdin:
    _, venta = line.strip().split("\t")
    venta = float(venta)

    # Sumamos la venta al total
    total_ventas += venta

# Imprimimos el resultado de las ventas totales
print(f"total\t{total_ventas}")
