import random
import time


def sequential_search(arr, ele):
    start = time.time()
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    end = time.time()
    return found, end - start


def ordered_sequential_search(arr, ele):
    start = time.time()
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    end = time.time()
    return found, end - start


def binary_search_iterative(arr, ele):
    start = time.time()
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] == ele:
            found = True
        else:
            if ele < arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end - start


def binary_search_recursive(arr, ele):
    start = time.time()
    if len(arr) == 0:
        end = time.time()
        return False, end - start
    else:
        midpoint = len(arr) // 2
        if arr[midpoint] == ele:
            end = time.time()
            return True, end - start
        else:
            if ele < arr[midpoint]:
                return binary_search_recursive(arr[:midpoint], ele)
            else:
                return binary_search_recursive(arr[midpoint + 1:], ele)


def generate_lists():
    lists = []
    for i in [500, 1000, 10000]:
        for j in range(100):
            lst = random.sample(range(i * 10), i)
            lists.append(lst)
    return lists


def main():
    lists = generate_lists()

    for i, lst in enumerate(lists):
        print(f"List {i + 1}")
        for size in [500, 1000, 10000]:
            ele = -1
            print(f"List size: {size}")
            
            total_time = 0
            for j in range(100):
                found, time_taken = sequential_search(lst, ele)
                total_time += time_taken
            avg_time = total_time / 100
            print("Sequential Search took %10.7f seconds to run, on average" % avg_time)
            
            total_time = 0
            for j in range(100):
                found, time_taken = ordered_sequential_search(lst, ele)
                total_time += time_taken
            avg_time = total_time / 100
            print("Ordered Sequential Search took %10.7f seconds to run, on average" % avg_time)
            
            total_time = 0
            for j in range(100):
                found, time_taken = binary_search_iterative(lst, ele)
                total_time += time_taken
            avg_time = total_time / 100
            print("Binary Search Iterative took %10.7f seconds to run, on average" % avg_time)
            
            total_time = 0
            for j in range(100):
                found, time_taken = binary_search_recursive(lst, ele)
                total_time += time_taken
            avg_time = total_time / 100
            print("Binary Search Recursive took %10.7f seconds to run, on average" % avg_time)


if __name__ == '__main__':
    main()
