# coding:utf-8
from functools import reduce
def fact(n):
    '''returns n!'''
    return  1 if n < 2 else n * fact(n-1)
def add(x,y):
    return x+y

if __name__ == '__main__':
    #函数式编程的特点就是使用高阶函数
    print(list(map(fact,range(6))))
    print(list(map(fact,filter(lambda n:n%2,range(6)))))
    #map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的结果list返回。
    print(reduce(add,range(100)))
    #再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    pass