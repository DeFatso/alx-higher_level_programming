#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)
if (int(last[-1])) < 6 and (int(last[-1])) != 0:
    print('Last digit of {} is {} and is less than 6 and\
             not 0'.format(int(number), int(last[-1])))
elif (int(last[-1])) == 0:
    print('Last digit of {} is {} and is 0'.format(int(number), int(last[-1])))
else:
    print('Last digit of {} is {} and is greater\
             than 5'.format(int(number), int(last[-1])))
