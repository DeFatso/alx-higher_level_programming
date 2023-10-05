#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add
    result = add(a, b)
    print('{} + {} = {}'.format(a, b, result))

    from calculator_1 import sub
    result = sub(a, b)
    print('{} - {} = {}'.format(a, b, result))

    from calculator_1 import mul
    result = mul(a, b)
    print('{} * {} = {}'.format(a, b, result))

    from calculator_1 import div
    result = div(a, b)
    print('{} / {} = {}'.format(a, b, result))
