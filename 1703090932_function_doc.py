# coding:utf-8

def factorial(n):
    '''returns n!'''
    return  1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(20))
    print(factorial.__doc__)
    print(type(factorial))
    print(help(factorial))

    fact = factorial
    print(fact)
    print(fact(5))
    print(map(factorial,range(11)))
    print(list(map(fact,range(11))))
    pass