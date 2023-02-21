import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end = time.time()
    return end - start


def shell_sort(a_list):
    start = time.time()
    sublistcount = len(a_list)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(a_list,startposition,sublistcount)

        sublistcount = sublistcount // 2
    end = time.time()
    return end - start


def gap_insertion_sort(alist, start, gap):

    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    start = time.time()
    sorted_list = sorted(a_list)
    end = time.time()
    return end - start


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 10000]

    for the_size in list_sizes:
        total_time_insertion = 0
        total_time_shell = 0
        total_time_python = 0

        for i in range(100):
            my_list = get_me_random_list(the_size)

            time_insertion = insertion_sort(my_list)
            total_time_insertion += time_insertion

            time_shell = shell_sort(my_list)
            total_time_shell += time_shell

            time_python = python_sort(my_list)
            total_time_python += time_python

        avg_time_insertion = total_time_insertion / 100
        avg_time_shell = total_time_shell / 100
        avg_time_python = total_time_python / 100

        print(f"For a list of {the_size} elements:")
        print(f"Insertion sort took {avg_time_insertion:.7f} seconds to run, on average")
        print(f"Shell sort took {avg_time_shell:.7f} seconds to run, on average")
        print(f"Python sort took {avg_time_python:.7f} seconds to run, on average")
