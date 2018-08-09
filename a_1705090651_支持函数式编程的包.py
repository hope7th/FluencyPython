#coding:utf-8
from functools import reduce
from operator import mul
from operator import itemgetter

# def fact(n):
#     return reduce(lambda a,b:a*b,range(1,n+1))

def fact(n):
    return reduce(mul,range(1,n+1))

#mul 函数计算阶乘

if __name__ == '__main__':
    metro_data = [
        (' Tokyo', 'JP', 36.933, (35.689722, 139.691667)), (' Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        (' Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        (' New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        (' Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    for city in sorted(metro_data,key=itemgetter(2)):
        print(city)
    print(fact(10))
