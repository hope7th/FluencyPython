# coding:utf-8
from functools import reduce

def fact(n):
    '''返回阶乘'''
    return 1 if n < 2 else n * fact(n-1)


if __name__ == '__main__':
    #在运行时候创建
    #能赋值给变量，或数据结构中得元素
    #作为参数
    #作为函数返回结果

    print(fact(42))
    print(fact.__doc__)
    print(type(fact))

    #函数赋值
    fact1 = fact
    print(fact1)
    print(fact1(5))

    #当参数传递
    print(list(map(fact1,range(11))))
    pass