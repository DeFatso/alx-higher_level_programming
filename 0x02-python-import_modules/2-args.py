#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    sep = ': '

    if argc == 0:
        print('0 arguments.')
    else:
        if argc == 1:
            print('{} argument'.format(argc))
        else:
            print('{} arguments'.format(argc))

    for i in range(1, len(sys.argv)):
        argument = sys.argv[i]
        print(f'{i}{sep}{argument}')
