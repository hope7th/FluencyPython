# -*- coding:utf-8 -*-

class Province:
    country = "中国"
    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    obj = Province("山西省")
    obj.perple = "黄种人"
    print obj.name
    print obj.country
    print obj.country
    Province.country="米国"
    print Province.country
    print obj.country
    print obj.perple