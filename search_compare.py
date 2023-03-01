import random
import time

def sequential_search(lst, x):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(lst) and not found:
        if lst[pos] == x:
            found = True
        else:
            pos = pos + 1

    elapsed_time = time.time() - start_time
    return found, elapsed_time

def ordered_sequential_search(lst, x):
    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(lst) and not found and not stop:
        if lst[pos] == x:
            found = True
        else:
            if lst[pos] > x:
                stop = True
            else:
                pos = pos+1

    elapsed_time = time.time() - start_time
    return found, elapsed_time

def binary_search_iterative(lst, x):
    start_time = time.time()
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == x:
            found = True
        else:
            if x < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    elapsed_time = time.time() - start_time
    return found, elapsed_time

def binary_search_recursive(lst, x):
    start_time = time.time()

    if len(lst) == 0:
        elapsed_time = time.time() - start_time
        return False, elapsed_time
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == x:
            elapsed_time = time.time() - start_time
            return True, elapsed_time
        else:
            if x < lst[midpoint]:
                elapsed_time = time.time() - start_time
                return binary_search_recursive(lst[:midpoint], x)[0], elapsed_time
            else:
                elapsed_time = time.time() - start_time
                return binary_search_recursive(lst[midpoint + 1:], x)[0], elapsed_time

def insertion_sort(lst):
    start_time = time.time()
    for i in range(1, len(lst)):
        current_val = lst[i]
        position = i

        while position > 0 and lst[position - 1] > current_val:
            lst[position] = lst[position - 1]
            position = position - 1

        lst[position] = current_val

    elapsed_time = time.time() - start_time
    return lst, elapsed_time

def shell_sort(lst):
    start_time = time.time()
    sublistcount = len(lst) // 2

    while sublistcount > 0:
        for startpos in range(sublistcount):
            gap_insertion_sort(lst, startpos, sublistcount)

        sublistcount = sublistcount // 2

    elapsed_time = time.time() - start_time
    return lst, elapsed_time

def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        current_val = lst[i]
        position = i

        while position >= gap and lst[position - gap] > current_val:
            lst[position] = lst[position - gap]
            position = position - gap

        lst[position] = current_val

def python_sort(lst):
    start_time = time.time()
    lst.sort()
    elapsed_time = time.time() - start_time
    return
