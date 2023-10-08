#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []

    for num in my_list:
        div_by = my_list[num] % 2 == 0
        result.append(div_by)
    return result
