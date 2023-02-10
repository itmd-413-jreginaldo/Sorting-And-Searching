"""
Python Sorting and Searching

This program will visualize the different speeds of three different sorting techniques, bubble sort, shell sort, and
quick sort. The program will output graphs showings the "Time vs Size of Data" relationships per sorting technique.
"""

import time
import random
import matplotlib.pyplot as plt

"""
CREDIT: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
"""
def bubble_sort(data):
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
CREDIT: https://www.programiz.com/dsa/shell-sort
"""
def shell_sort(array, n):
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
CREDIT: https://www.programiz.com/dsa/quick-sort
"""
# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


if __name__ == '__main__':
    print("Hi")
