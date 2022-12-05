#!/usr/bin/bash
def print_list_integer(my_list=[]):
    for i in my_list:
        if type(i) != int:
            continue
        print('{}'.format(i))