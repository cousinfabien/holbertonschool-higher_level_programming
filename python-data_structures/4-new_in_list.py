#!/usr/bin/python3
def new_in_list (list, id, element):
    listcopy = list.copy()
    if id < 0 or id >= len(list):
        return listcopy
    listcopy[id] = element
    return listcopy
