#coding:utf-8

from inspect import signature


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
    sig = signature(clip)
    print(sig)
    print(str(sig))
    for name,param in sig.parameters.items():
        print(param.kind,":",name,"=",param.default)
    my_tag = {
        'name': 'img',
        'title': 'sunset',
        'src': 'sunset.jpg',
        'cls': 'framed'
    }
    sig2 = signature(tag)
    bound_args = sig2.bind(**my_tag)
    print(bound_args)
    for name,value in bound_args.arguments.items():
        print(name,"=",value)
    del my_tag['name']
    bound_args = sig2.bind(**my_tag)
    
    pass