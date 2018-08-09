# coding:utf-8

def clip(text,max_len=12):
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
    print(clip("asdasdassa   sda "))
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)
    #下， 这 里 不 包 含 前 缀 为 * 或 ** 的 变 长 参 数。
    pass
