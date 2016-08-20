# -*- coding: utf-8 -*-
#求一个数的平方根
def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x/y)/2
    return y
    
#将一个输入的数字字符转换成浮点数
ridicand = float(raw_input('pls enter any number above zero: '))
print sqrt(ridicand)