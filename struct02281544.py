# coding:utf-8
import struct

if __name__ == '__main__':
    fmt = '<3s3sHH'
    with open('haha.gif','rb') as fp:
        img = memoryview(fp.read())
    print(img)
    header = img[:10]
    print(bytes(header))
    print(struct.unpack(fmt,header))
    del header
    del img
    #struct 模 块 提 供 了 一 些 函 数， 把 打 包 的 字 节 序 列 转 换 成 不 同 类 型 字 段 组 成 的 元 组，
    #  还 有 一 些 函 数 用 于 执 行 反 向 转 换， 把 元 组 转 换 成 打 包 的 字 节 序 列。
