#!/usr/bin/python3

def text_indentation(text):
    """ prints a text with 2 new lines after delimeter"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split('\n')

    for line in lines:
        line = line.strip()

        if line:
            for char in line:
                print(char, end='')

                if char in ['.', '?', ':']:
                    print('\n\n', end='')
                else:
                    print(end='')
            print()
