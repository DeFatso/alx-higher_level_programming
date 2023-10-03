#!/usr/bin/python3

for i in range(122, 96, -2):
    lower = chr(i)
    for j in range(89, 64, -2):
        upper = chr(j)
        print('{}{}'.format(upper, lower), end='')
