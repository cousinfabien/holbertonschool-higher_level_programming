#!/usr/bin/python3
def new_in_list(my_list, id, element):
    listcopy = my_list.copy()
    if id < 0 or id >= len(my_list):
        return listcopy
    listcopy[id] = element
    return listcopy
