# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:14:03 2024

@author: TranHuynhTuTrinh
"""
"""
Viết phương thức kiểm tra giá trị nhập vào phải thuộc đoạn [-89, 90], nếu 
sai bắt nhập lại (Chú ý: không dùng đệ quy).
"""
def ktra_giatri():
    gtri = input("Nhập giá trị: ")
    if gtri.replace('.','',1).replace('-','',1).isdigit():
        gtri = float(gtri)
    if -89 <= gtri <= 90:
        return gtri
    print("Không hợp lệ, nhập lại")
    return ktra_giatri()
print(ktra_giatri())
