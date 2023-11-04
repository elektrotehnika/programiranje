# -*- coding: utf-8 -*-
"""
Пример 1 - Израчунавање факторијела произвољног броја коришћењем итеративног 
алгоритма.
"""

def faktorijel_iterativno(n):
    rezultat = 1
    while n > 1:
        rezultat *= n
        n -= 1
    return rezultat

#print(faktorijel_iterativno(4))

"""
Пример 2 - Израчунавање факторијела произвољног броја коришћењем рекурзивног 
алгоритма.
"""

def faktorijel_rekurzivno(n):
    if n <= 1:
        return 1
    return n*faktorijel_rekurzivno(n-1)

print(faktorijel_rekurzivno(4))