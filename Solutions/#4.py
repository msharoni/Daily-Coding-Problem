'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def func(List):
    smallest = 0
    for num in List:
        if num > 0:
            smallest = num
            break
    for num in List:
        if num > 0 and num < smallest:
            smallest = num
    if smallest != 1:
        return smallest-1
    else:
        while(True):
            smallest += 1
            if smallest not in List:
                return smallest
def func2(List):
    i=1
    while i in List:
        i += 1
    return i
print(func2([3, 4, -1, 1]))
