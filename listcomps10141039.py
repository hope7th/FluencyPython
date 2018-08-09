# coding=utf-8

if __name__ == '__main__':
    symbols = '$%^&*#@￥'
    codes = [ord(symbol) for symbol in symbols]
    beyond_ascii1 = [ord(s) for s in symbols if ord(s)>127]
    beyond_ascii2 = list(filter(lambda c:c>127,map(ord,symbols)))
    print beyond_ascii1
    print beyond_ascii2
    #map函数不是改变原有的list，而是返回新的list
    #print codes

    colors = ['black','white']
    sizes = ['s','m','l']
    tshirts = [(color,size) for color in colors for size in sizes]
    print tshirts
