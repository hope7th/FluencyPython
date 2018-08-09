# coding:utf-8
import random
class BingoCage:
    def __init__(self,items):
        print("imhere_init")
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingCage")

    def __call__(self, *args, **kwargs):
        print("imhere_call")
        #bingo() 实例直接作为函数调用
        return self.pick()



if __name__ == '__main__':
    #不仅Python函数是真正的对象，任何Python对象都可以表现得像函数。为此，只需实现实例方法__call__。
    #bingo.pick() 的 快 捷 方 式 是 bingo()。
    bingo = BingoCage(range(7))
    print(bingo._items)
    print(bingo.pick())
    print(bingo())
    pass