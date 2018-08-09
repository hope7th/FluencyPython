#coding:utf-8
from operator import itemgetter
from collections import namedtuple
from operator import attrgetter

#itemgetter(1),lambda fields:fields[1],接受集合的函数，返回索引为1的元素

if __name__ == '__main__':
    metro_data = [(' Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
                  (' Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
                  (' Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
                  (' New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
                  (' Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
    for city in sorted(metro_data,key=itemgetter(1)):
        print(city)

    cc_name = itemgetter(1,0)
    for city in metro_data:
        print(cc_name(city))
    #itemgetter 会返回提取的值构成的元组

    LatLong = namedtuple('LatLong','lat long')
    Metropolis = namedtuple('Metropolis','name cc pop coord')
    metro_areas = [Metropolis(name,cc,pop,LatLong(lat,long)) for name,cc,pop,(lat,long) in metro_data]
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)
    name_lat = attrgetter('name','coord.lat')
    for city in sorted(metro_areas,key=attrgetter('coord.lat')):
        print(name_lat(city))


    pass