import random
import time


def naive_search(lists, target):
    for i in range(len(lists)):
        if lists[i] == target:
            return i

    return -1


def binary_search(lists, target, low=None, high=None):       # low and high points to the indexes of the list not the element in the list
    if low is None:
        low = 0
    if high is None:
        high = len(lists) - 1

    midpoint = (low + high) // 2

    if lists[midpoint] == target:
        return midpoint

    elif lists[midpoint] > target:
        return binary_search(lists, target, low, midpoint - 1)

    else:   # lists[midpoint] < target
        return binary_search(lists, target, midpoint + 1, high)


if __name__ == '__main__':

    lists = [1, 2, 4, 5, 6, 10, 20, 50]
    target = 10
    print(naive_search(lists, target))
    print(binary_search(lists, target))

# here the binary search is faster and better than naive search. So, binary search is much more preferable than the naive search.


# example for the amount of time to execute the search for both naive and binary
# if __name__ == '__main__':
#     length = 1000
#     sorted_list = set()
#     while len(sorted_list) < length:
#         sorted_list.add(random.randint(-2*length, 2*length))
#
#     sorted_list = sorted(list(sorted_list))
#
#     start = time.time()   # starts a stopwatch and starts recording the time
#     for target in sorted_list:
#         naive_search(sorted_list, target)
#
#     end = time.time()
#     print(start - end)
#
#     start = time.time()  # starts a stopwatch and starts recording the time
#     for target in sorted_list:
#         binary_search(sorted_list, target)
#
#     end = time.time()
#     print(start - end)
