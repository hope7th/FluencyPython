#coding:utf-8
from inspect import signature

def clip(text,max_len:'int > 0'=80)->str:
    '''在max_len前面或后面的空格处截断文本'''

    end = None

    if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ',max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    print(end)
    return text[:end].rstrip()

if __name__ == '__main__':
    #打印函数的注解Python 对 注 解 所 做 的 唯 一 的 事 情 是， 把 它 们 存 储 在 函 数 的 __annotations__ 属 性 里。
    print(clip.__annotations__)
    #取出函数的注解
    sig = signature(clip)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note,':',param.name,'=',param.default)

    #ljust ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
     #repr() 函数将对象转化为供解释器读取的形式。
    pass