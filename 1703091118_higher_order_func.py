# coding:utf-8

if __name__ == '__main__':
    # 接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher - orderfunction）。map函数就是一例，如示例5 - 2
    # 所示。此外，内置函数sorted也是.
    fruits = [' strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits,key=len))