# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:57:00 2024

@author: TranHuynhTuTrinh
"""
"""
Viết phương thức kiểm tra một số nhập vào là số chẵn có giá trị âm. Đúng 
trả về true. Sai trả về false.
"""
def ktra_so(n):
    return n < 0 and n%2 == 0
print(ktra_so(-10))
