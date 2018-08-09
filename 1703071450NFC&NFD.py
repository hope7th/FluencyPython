# coding:utf-8
from unicodedata import normalize

if __name__ == '__main__':
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1,s2)
    print(len(s1),len(s2))
    print(s1==s2)
    # NFC
    print(len(normalize('NFC',s1)),len(normalize('NFC',s2)))
    print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
    print(normalize('NFD', s1)==normalize('NFD', s2))
    print(normalize('NFC', s1) == normalize('NFC', s2))
    #NFC（ Normalization Form C） 使 用 最 少 的 码 位 构 成 等 价 的 字 符 串， 而 NFD 把 组 合 字 符 分 解 成 基 字 符 和 单 独 的 组 合 字 符。
    pass