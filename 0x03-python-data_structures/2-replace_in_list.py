#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idxx = str(idx)
    if (idx >= 0) and (idx < len(my_list) and idx.isdigit()):
        my_list[idx] = element
        return my_list
