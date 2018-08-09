# -*- coding:utf-8 -*-
import bisect
import sys
import random
import time
HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,16,29,30]
NEEDLES = [0,1,2,5,8,9,10,22,23,29,30,31,32]


ROW_FMT = '{0:2d}@{1:2d} {2}{0:2d}'
#0,1,2,0 参数索引从零开始
def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK,needle)
        #print position
        offset = position * ' |'
        print offset
        print '---------------------------'
        print ROW_FMT.format(needle,position,offset)
        # if needle==31:
        #     break
def grade(score,breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    print i
    return grades[i]

if __name__ == '__main__':
    print sys.argv
    # print sys.argv[-1]
    # print sys.argv[0]
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right
    print 'DEMO:',bisect_fn.__name__
    print 'haystack->',''.join('%2d '%n for n in HAYSTACK)
    demo(bisect_fn)

    print [grade(score) for score in [33,99,77,70,89,69]]

    SIZE = 7
    random.seed(1729)
    #？？？这行代码是什么意思
    my_list = []
    print random.random()
    random.seed(1729)
    print random.random()
    for i in range(SIZE):
        new_item= random.randrange(SIZE*2)
        bisect.insort(my_list,new_item)
        print '%2d'%new_item,my_list
        #？？？这行代码怎么打印的
    l = [1,2,5]
    print l*5
    print 5 * 'abcd'
    board = [['_']*3]
    print board
    board = [['_']*3 for i in range(3)]
    print board
    board[1][2] = 'x'
    print board
    weird_board = [['_']*3]*3
    print "weird_board"
    print weird_board
    weird_board[1][2] = '0'
    print weird_board

    #weird_board实际上是三个指向同一列表的引用
    #board是三个列表

    row=['_']*3
    board3=[]
    for i in range(3):
        board3.append(row)

    board4 = []
    for i in range(3):
        row=['_']*3
        board4.append(row)

    board3[2][0]='X'
    print board3

    board4[2][0]='y'
    print board4

    l = [1,2,4]
    print id(l)
    #id方法的返回值是对象的内存地址
    l*=2
    print l
    print id(l)
    t = (1,2,3)
    t*=2
    print t
    print id(t)
    #time.sleep(1)
    t2 = (1,2,[30,40])
    try:
        t2[2]+=[50,60]
    except:
        print "t2"
        print t2

    t3 = (1,2,[30,40])
    t3[2].extend([51,61])
    print t3
    
    #python - m dis test.py 这个方法用于查看汇编语言
    pass