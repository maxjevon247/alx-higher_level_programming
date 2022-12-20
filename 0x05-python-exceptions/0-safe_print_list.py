#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    valid_num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], "\n")
            valid_num += 1
        except (IndexError, ValueError, TypeError):
            break
    print("")
    return (valid_num)
