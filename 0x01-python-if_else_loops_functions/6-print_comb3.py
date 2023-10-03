#!/usr/bin/python3
for number in range(10):
    for number2 in range(number + 1, 10):
        print('{}{}, '.format(number, number2), end='')
print('\n', end='')
