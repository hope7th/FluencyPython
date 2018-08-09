# -*- coding:utf-8 -*-

if __name__ == '__main__':
    city = 'São Paulo'
    print(city.encode('utf-8'))
    print(city.encode('utf-16'))
    print(city.encode('iso8859_1'))
    print(city.encode('cp437',errors='ignore'))
    print(city.encode('cp437', errors='replace'))
    print(city.encode('cp437', errors='xmlcharrefreplace'))
    #'xmlcharrefreplace' 把 无 法 编 码 的 字 符 替 换 成 XML 实 体。