#coding:utf-8

def factorial(n):
    '''renturn n!'''
    return 1 if n<2 else  n * factorial(n-1)

class C:pass
def func():pass

if __name__ == '__main__':
    #探知函数的属性
    #_dict_属性的使用,储存赋它的用户属性
    factorial.short_name = "fact"
    print(dir(factorial))
    print("函数的赋值属性")
    print(factorial.short_name)

    #函数有而常规对象没有得属性
    obj_c = C()
    print("函数有而常规对象没有得属性")
    print(sorted(set(dir(func))-set(dir(obj_c))))