# -*- coding:utf-8 -*-
#python3.6下测试
import array
if __name__ == '__main__':
    cafe = bytes('cafè',encoding='utf-8')
    print cafe
    print cafe[0]
    print cafe[:1]

    cafe_arr = bytearray(cafe)
    print cafe_arr
    print cafe_arr[-1:]
    # 字符串类str里有一个encode()
    # 方法，它是从字符串向比特流的编码过程。而bytes类型恰好有个decode()
    # 方法，它是从比特流向字符串解码的过程
    numbers = array.array(' h', [-2, -1, 0, 1, 2])
    #指定类型代码h,创建一个短整型数组
    octets = bytes(numbers)
    print octets


