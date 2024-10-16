# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:40:25 2024

@author: TranHuynhTuTrinh
"""
"""
Áp dụng kỹ thuật kwargs, *args, ** kwargs thiết kế hàm tính chu vi, diện 
tích hình vuông, hình chữ nhật, hình tròn theo các phương pháp gọi hàm 
sau:
tinh(10, hinh='vuong', tinh='cv')
tinh(50, hinh='vuong', tinh='dt')
tinh(18, hinh='tron', tinh='cv')
tinh(20, 30, hinh='chu_nhat', tinh='cv')
"""
import math
def tinh(*args, **kwargs):
    hinh = kwargs.get("hinh")
    pheptinh = kwargs.get("tinh")
    
    if hinh == "vuong":
        canh = args[0]
        return 4 * canh if pheptinh == "cv" else canh ** 2
    
    elif hinh == "chu_nhat":
        dai = args[0]
        rong = args[1]
        return 2 * (dai + rong) if pheptinh == "cv" else dai * rong
    
    elif hinh == "tron":
        bankinh = args[0]
        return 2 * math.pi * bankinh if pheptinh == "cv" else math.pi* (bankinh ** 2)
    
    else:
        return "Hình không hợp lệ"
    
if __name__=="__main__":
    print(tinh(10, hinh="vuong", tinh="cv"))
    print(tinh(50, hinh="vuong", tinh="dt"))
    print(tinh(18, hinh="tron", tinh="cv"))
    print(tinh(20, 30, hinh="chu_nhat", tinh="cv"))
    