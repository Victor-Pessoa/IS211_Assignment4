import random
import time

def sequential_search(lst, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
        else:
            pos = pos+1

    end_time = time.time()
    return found, end_time-start_time


def ordered_sequential_search(lst, item):
    lst.sort()
    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(lst) and not found and not stop:
        if lst[pos] == item:
            found = True
        else:
            if lst[pos] > item:
                stop = True
            else:
                pos = pos+1

    end_time = time.time()
    return found, end_time-start_time


def binary_search_iterative(lst, item):
    lst.sort()
    start_time = time.time()
    first = 0
    last = len(lst)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    end_time = time.time()
    return found, end_time-start_time


def binary_search_recursive(lst, item):
    lst.sort()
    start_time = time.time()

    if len(lst) == 0:
        end_time = time.time()
        return False, end_time-start_time
    else:
        midpoint = len(lst)//2
        if lst[midpoint]==item:
            end_time = time.time()
            return True, end_time-start_time
        else:
            if item < lst[midpoint]:
                end_time = time.time()
                return binary_search_recursive(lst[:midpoint], item)[0], end_time-start_time
            else:
                end_time = time.time()
                return binary_search_recursive(lst[midpoint+1:], item)[0], end_time-start_time


def generate_lists():
    lists = {}
    for size in [500, 1000, 10000]:
        for i in range(100):
            lst = random.sample(range(1, size+1), size)
            lists[f'{size}_{i}'] = lst
    return lists


def main():
    lists = generate_lists()
    for size in [500, 1000, 10000]:
        seq_sum = ord_seq_sum = bin_it_sum = bin_rec_sum = 0
        for i in range(100):
            lst = lists[f'{size}_{i}']
            result, time_taken = sequential_search(lst, -1)
            seq_sum += time_taken

            result, time_taken = ordered_sequential_search(lst, -1)
            ord_seq_sum += time_taken

            result, time_taken = binary_search_iterative(lst, -1)
            bin_it_sum += time_taken

            result, time_taken = binary_search_recursive(lst, -1)
            bin_rec_sum += time_taken

        print(f"Sequential Search took {total_time_seq / 100:.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {total_time_ord_seq / 100:.7f} seconds to run, on average")
        print(f"Binary Search (Iterative) took {total_time_bin_iter / 100:.7f} seconds to run, on average")
        print(f"Binary Search (Recursive) took {total_time_bin_rec / 100:.7f} seconds to run, on average")

    if __name__ == "__main__":
        main()
