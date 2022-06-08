#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = my_list[:]
    for i in range(len(replaced)):
        if replaced[i] == search:
            replaced[i] = replace
    return replaced
