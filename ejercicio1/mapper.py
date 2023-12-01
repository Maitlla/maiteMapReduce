#!/usr/bin/python
import sys

for line in sys.stdin:
    if line.count("\t")==5:
        data = line.strip().split("\t")
        date, time, store, item, cost, payment = data
        print(store+"\t"+cost)


