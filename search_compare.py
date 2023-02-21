import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    # Create a list of integers from 0 to n-1
    a_list = list(range(n))
    # Shuffle the list randomly
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    """
    Sequential search function
    
    :params: a_list: List to be searched
             item: Element to search for
    :returns: True if item is found in the list, False otherwise
    """
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

def ordered_sequential_search(a_list, item):
    """
    Ordered sequential search function
    
    :params: a_list: List to be searched (must be sorted in ascending order)
             item: Element to search for
    :returns: True if item is found in the list, False otherwise
    """
    pos = 0
    found = False
    stop = False
    
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

def binary_search_iterative(a_list,item):
    """
    Iterative binary search function
    
    :params: a_list: List to be searched (must be sorted in ascending order)
             item: Element to search for
    :returns: True if item is found in the list, False otherwise
    """
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

def binary_search_recursive(a_list,item):
    """
    Recursive binary search function
    
    :params: a_list: List to be searched (must be sorted in ascending order)
             item: Element to search for
    :returns: True if item is found in the list, False otherwise
    """
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

if __name__ == "__main__":
    # Define the sizes of the random lists to be generated
    sizes = [500, 1000, 10000]

    for size in sizes:
        # Initialize the total time for each search algorithm
        total_time_seq = 0
        total_time_ord_seq = 0
        total_time_bin_iter = 0
        total_time_bin_rec = 0
        
        # Generate 100 random lists of the current size and search for -1 in each list
        for i in range(100):
