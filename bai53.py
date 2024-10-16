# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:38:51 2024

@author: TranHuynhTuTrinh
"""
#Nhập vào một số nguyên dương n và viết các phương thức sau
#a) S = 1 + 2 + 3 +......+ n
import math
def tong(n):
    S = 0
    for i in range(1, n + 1):
        S += i
    return S

#b) S = 1^2 +2^2 +3^2 +......+n^2
def tong_binhphuong(n):
    S = 0
    for i in range(1, n + 1):
        S += i ** 2
    return S

#c) S = 1 + 1/2 + 1/3 +......+ 1/n
def tong_phanso(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / i
    return S

#d) S = 1! + 2! + 3! +......+ n!
def tong_giaithua(n):
    S = 0
    for i in range(1, n + 1):
       giaithua = 1
       for j in range(1, i + 1):
           giaithua *= j
       S += giaithua
    return S

#e) S = 1 * 2 * 3 *......* n
def tich(n):
    S = 1
    for i in range(1, n + 1):
        S *= i
    return S

if __name__== '__main__':
    print(tong(10))
    print(tong_binhphuong(5))
    print(tong_phanso(7))
    print(tong_giaithua(9))
    print(tich(20))
    