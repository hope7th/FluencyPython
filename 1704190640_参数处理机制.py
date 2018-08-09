#coding:utf-8

def tag(name,*content,cls=None,**attrs):
    if cls is not None:
        attrs['class']=cls

    if attrs:
        attr_str = ''.join(' %s="%s"'%(attr,value) for attr,value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s<%s>'%(name,attr_str,c,name) for c in content)
    else:
        return '<%s%s/>'%(name,attr_str)
    pass
if __name__ == '__main__':
    # 关键字参数会被**attrs捕获
    #任意参数会被*content捕获
    #cls只能通过关键字参数指定
    #
    print(tag('br'))
    print(tag('p','hello'))
    print(tag('p','hello','world'))
    print(tag('p','hello',id=33))
    print(tag('p','hello','world',cls='sidebar'))
    print(tag(name="img",content="testing"))
    my_tag = {
        'name':'img',
        'title':'sunset',
        'src':'sunset.jpg',
        'cls':'framed'
    }
    #在 my_tag 前 面 加 上 **， 字 典 中 的 所 有 元 素 作 为 单 个 参 数 传 入， 同 名 键 会 绑 定 到 对 应 的 具 名 参 数 上， 余 下 的 则 被 ** attrs 捕 获。
    print(tag(**my_tag))
    pass