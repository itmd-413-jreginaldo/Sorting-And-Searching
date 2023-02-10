"""
Python Sorting and Searching

This program will visualize the different speeds of three different sorting techniques, bubble sort, shell sort, and
quick sort. The program will output graphs showings the "Time vs Size of Data" relationships per sorting technique.
"""
import sys
import time
import random
import matplotlib.pyplot as plt

"""
Bubble Sort Algo
CREDIT: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
"""
def bubble_sort_algo(data):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(data) - 1, 0, -1):
        for i in range(n):
            if data[i] > data[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                data[i], data[i + 1] = data[i + 1], data[i]
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return


"""
Shell Sort Algo
CREDIT: https://www.programiz.com/dsa/shell-sort
"""


def shell_sort_algo(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


"""
Quick Sort Algo
CREDIT: https://www.geeksforgeeks.org/python-program-for-quicksort/
"""
# function to find the partition position
# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


def quick_sort_algo(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort_algo(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort_algo(array, pi + 1, high)


def determine_time_bubble(data):
    start_time = time.time()  # start the clock
    bubble_sort_algo(data)  # put your sorting method
    stop_time = time.time() - start_time  # stop the clock and calculate the time difference
    print(f"Bubble Sort of {len(data)} elements took {stop_time:.2f}s")

    return stop_time


def determine_time_shell(data):
    start_time = time.time()  # start the clock
    shell_sort_algo(data, len(data))  # put your sorting method
    stop_time = time.time() - start_time  # stop the clock and calculate the time difference
    print(f"Shell Sort of {len(data)} elements took {stop_time:.2f}s")

    return stop_time


def determine_time_quick(data):
    start_time = time.time()  # start the clock
    # quick_sort_algo(data, 0, len(data) - 1)  # put your sorting method
    quick_sort_algo(data, 0, len(data) - 1)
    stop_time = time.time() - start_time  # stop the clock and calculate the time difference
    print(f"Quick Sort of {len(data)} elements took {stop_time:.2f}s")

    return stop_time


def generate_lists():
    # Lists to store different ranges of data
    ten_thousand_list = []
    thirty_thousand_list = []
    fifty_thousand_list = []
    seventy_thousand_list = []
    ninety_thousand_list = []

    # Lists to store different times achieved per dataset / per sort
    bubble_sort_time_list = []
    shell_sort_time_list = []
    quick_sort_time_list = []

    # Manually adjust recursion limit to fix recursion depth error from quick sort
    sys.setrecursionlimit(10 ** 6)

    for i in range(0, 10000):  # create 10000 random numbers
        x = random.randint(1, 10000)  # ranges 1 to 10000
        ten_thousand_list.append(x)

    bubble_sort_time_list.append(determine_time_bubble(ten_thousand_list))
    shell_sort_time_list.append(determine_time_shell(ten_thousand_list))
    quick_sort_time_list.append(determine_time_quick(ten_thousand_list))

    for i in range(0, 30000):  # create 30000 random numbers
        x = random.randint(1, 30000)  # ranges 1 to 30000
        thirty_thousand_list.append(x)

    bubble_sort_time_list.append(determine_time_bubble(thirty_thousand_list))
    shell_sort_time_list.append(determine_time_shell(thirty_thousand_list))
    quick_sort_time_list.append(determine_time_quick(thirty_thousand_list))

    for i in range(0, 50000):  # create 50000 random numbers
        x = random.randint(1, 50000)  # ranges 1 to 50000
        fifty_thousand_list.append(x)

    bubble_sort_time_list.append(determine_time_bubble(fifty_thousand_list))
    shell_sort_time_list.append(determine_time_shell(fifty_thousand_list))
    quick_sort_time_list.append(determine_time_quick(fifty_thousand_list))

    for i in range(0, 70000):  # create 70000 random numbers
        x = random.randint(1, 70000)  # ranges 1 to 70000
        seventy_thousand_list.append(x)

    bubble_sort_time_list.append(determine_time_bubble(seventy_thousand_list))
    shell_sort_time_list.append(determine_time_shell(seventy_thousand_list))
    quick_sort_time_list.append(determine_time_quick(seventy_thousand_list))

    for i in range(0, 90000):  # create 90000 random numbers
        x = random.randint(1, 90000)  # ranges 1 to 90000
        ninety_thousand_list.append(x)

    bubble_sort_time_list.append(determine_time_bubble(ninety_thousand_list))
    shell_sort_time_list.append(determine_time_shell(ninety_thousand_list))
    quick_sort_time_list.append(determine_time_quick(ninety_thousand_list))


def main():
    generate_lists()


if __name__ == '__main__':
    main()
