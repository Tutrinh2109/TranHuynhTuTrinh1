# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:18:17 2024

@author: TranHuynhTuTrinh
"""
#Viết phương thức in ra n phần tử của dãy Fibonacy.
def fibonacci(n):
    danhsach_fib = []
    a, b = 0, 1
    for i in range(n):
        danhsach_fib.append(a)
        a, b = b, a + b
    return danhsach_fib
print(fibonacci(10))
