# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:29:57 2024

@author: TranHuynhTuTrinh
"""
"""
Viết phương thức tính chu vi và diện tích hình chữ nhật khi biết độ dài 2 
cạnh. Sau đó vẽ hình chữ nhật ra màn hình bằng các dấu *. Phương thức 
tính chu vi, diện tích và phương thức vẽ hình chữ nhật phải độc lập nhau.
"""
def chu_vi_hcn(dai, rong):
    return 2 * (dai + rong)

def dien_tich_hcn(dai, rong):
    return dai * rong

def ve_hinh_chu_nhat(dai, rong):
    for i in range(rong):
        print('*' * dai)

if __name__ == '__main__':
    print("Chu vi la:", chu_vi_hcn(5,3))
    print("Dien tich la:",dien_tich_hcn(5,3))
    ve_hinh_chu_nhat(5,3)

