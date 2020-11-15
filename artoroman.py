# -*- coding: utf-8 -*-
"""

定义类实现阿拉伯数字和罗马数字的转化

@author: XinweiWen

"""

class ArtoRoman:
    def __init__(self,ar):
       self.ar = ar
    
    def artoroman(self):
        ar_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman_list = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman_num =" "
        
        for i in range(len(ar_list)):
            while self.ar >= ar_list[i]:
                  self.ar -= ar_list[i]
                  roman_num += roman_list[i]
        return roman_num

if __name__ == '__main__':
    n = int(input('请输入你想要转换的数字：'))
    num = ArtoRoman(n)
    print(num.artoroman())
   