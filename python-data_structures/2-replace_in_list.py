#!/usr/bin/python3
def replace_in_list(list, id, element):
    if id < 0 or id >= len(list):
        return list
    list[id] = element
    return list
