# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:07:13 2024

@author: TranHuynhTuTrinh
"""
"""
Viết phương thức kiểm tra một số nhập vào: nếu là số âm có giá trị lẻ thì 
trả về -1, nếu là số dương có giá trị chẵn thì trả về 1, trường hợp khác trả
về 0.
"""
def kiem_tra(n):
    if n < 0 and n % 2 != 0:
        return -1
    elif n > 0 and n % 2 == 0:
        return 1
    return 0
print(kiem_tra(3))
