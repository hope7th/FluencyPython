# -*- coding:utf-8 -*-
from collections import Counter
from itertools import combinations

if __name__ == '__main__':
    # 1
    x = 6
    y = 5
    x,y = y,x
    print x,y

    #2
    print "hello" if True else "World"

    #3
    nfc = ["Packers","49ers"]
    afc = ["Ravens","Patriots"]
    print nfc + afc
    print str(1) + " world"
    print '1' + "world"
    print 1,"world"
    print nfc,1

    #4
    print 5.0//2
    print 2**5
    print .3/.13
    print .3//.1

    #5
    x = 2
    if 3>x>1:
        print x
    if 1<x>0:
        print x

    #6
    for tmpa,tmpb in zip(nfc,afc):
        print tmpa +" vs. "+tmpb

   #7
    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for index,team in enumerate(teams):
        print index,team

    #8
    numbers = [1,2,3,4,5,6]
    even = [number for number in numbers if number%2 ==0]
    print even

    #9
    print {key:value for value,key in enumerate(teams)}

    #10
    items = [0]*3
    print items

    #11
    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print ", ".join(teams)
    print "".join(teams)

    #12
    data = {'user': 1, 'name': 'Max', 'three': 4}
    is_admin = data.get("admin",False)
    print is_admin

    #13
    x=[1,2,3,4,5,6]
    print x[:3]
    print x[1:5]
    print x[-3:]
    print x[::1]
    print x[::2]
    print x[1::2]

    #14
    for x in range(101):print x ; print"fizz"[x % 3 * 4::] + "buzz"[x % 5 * 4::] or x

    #15
    print Counter("hello")

    #16
    teams = ["Packers","49ers","Ravens","Patriots"]
    for game in combinations(teams,2):
        print game

    #17
    False = True
    if False:
        print "Hello"
    else:
        print "world"

