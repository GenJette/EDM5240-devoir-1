#coding: utf-8

donald = [format(donald) for donald in range(30000, 100000)]

mike = ["{:05d}".format(mike) for mike in range(0, 18000)]

print(donald, mike)
