# coding:utf-8

if __name__ == '__main__':
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(fruits[::-1])
    print(sorted(fruits,key=lambda word:word[::-1]))
    #调用类时会运行类的__new__方法创建一个实例，然后运行__init__方法，初始化实例，最后把实例返回给调用方。因为Pytho没有new运算符，所以调用类相当于调用函数。
    pass