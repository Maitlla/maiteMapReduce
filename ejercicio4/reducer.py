#!/usr/bin/python

import sys

maxima_absoluta = 0.0

for line in sys.stdin:
    # line.strip().split("\t") divide en dos partes la clave:valor 
    # se asigna la clave a: _  que se ignora, y el valor lo asignamos a: la variable venta
    _, venta = line.strip().split("\t")
    venta = float(venta)

    # Actualizamos la venta más alta absoluta
    maxima_absoluta = max(maxima_absoluta, venta)

# Imprimimos el resultado del máximo absoluto
print(f"total\t{maxima_absoluta}")
