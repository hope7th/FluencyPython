# coding:utf-8
import os

if __name__ == '__main__':
    fp = open('cafe.txt','w',encoding='utf-8')
    print(fp)
    fp.write('café')
    fp.close()
    print(os.stat('cafe.txt').st_size)
    fp2 = open('cafe.txt')
    print(fp2)
    print(fp2.read())
    fp3= open('cafe.txt',encoding='utf-8')
    print(fp3.read())
    fp4 = open('cafe.txt','rb')
    print(fp4)
    print(fp4.read())