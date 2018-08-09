# coding=utf-8
if __name__ == '__main__':
    lax_coordinates = (33.9452,-118.408056)
    print lax_coordinates
    city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)
    print city,year,pop,chg,area
    tra_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
    for passport in sorted(tra_ids):
        print ('%s/%s'%passport)
    for country,_ in tra_ids:
        print country

    latitude, longitude = lax_coordinates
    print latitude
    print longitude

    divmod(20,8)
    print divmod(20,8)
    t = (11,3)
    print divmod(*t)
    quotient, remainder = divmod(*t)
    print quotient,remainder

    #a, *b, c, d = range(5)
    # *args获取不确定变量的参数，只支持python3.7

    metro_areas = [{
        ('Tokyo','JP',36.933,(35.689722,139.691667)),
        (' Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        (' Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        (' New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        (' Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    }]
    #print '{:15}|{:^9}|{:^9}'.format('','lat.','long.')
    fmt = '{:15}|{:9.4f}|{:9.4f}'
    for name1, cc1, pop1,(latitude1,longitude1) in metro_areas:
        print name1

        #print fmt.format(name,latitude,longitude)






