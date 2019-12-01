import math;

def max_of_vector(vector):
    return max(vector)


def min_of_vector(vector):
    return min(vector)


def sum_positive_vector(vector):
    result = 0
    for item in vector:
        if item > 0:
            result += item
    return result


def count_positive_vector(vector):
    result = 0
    for item in vector:
        if item > 0:
            result += 1
    return result;


def lab1_task1(vector_a, vector_b, vector_c):
    return (max_of_vector(vector_a) + min_of_vector(vector_b)) * 2.3 + max_of_vector(vector_c)


def func1(x):
    return math.sin(math.pow(x, 2)) + 1


def func2(x):
    return math.pow(x, 3) + 2.5
