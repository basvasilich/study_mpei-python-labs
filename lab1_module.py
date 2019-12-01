import math
from typing import Callable


def max_of_vector(vector: list) -> float:
    return max(vector)


def min_of_vector(vector: list) -> float:
    return min(vector)


def sum_positive_vector(vector: list) -> float:
    result = 0
    for item in vector:
        if item > 0:
            result += item
    return result


def count_positive_vector(vector: list) -> int:
    result = 0
    for item in vector:
        if item > 0:
            result += 1
    return result


def lab1_task1(vector_a: list, vector_b: list, vector_c: list) -> float:
    return (max_of_vector(vector_a) + min_of_vector(vector_b)) * 2.3 + max_of_vector(vector_c)


def func1(x: float):
    return math.sin(math.pow(x, 2)) + 1


def func2(x: float):
    return math.pow(x, 3) + 2.5


def make_row(var: float, f1: Callable[[float], str], **keyword_parameters: Callable[[float], str]) -> str:
    if 'f2' in keyword_parameters:
        return f"{str(var):6.4}{str(f1(var)):6.4}{str(keyword_parameters['f2'](var)):6.4}\n"
    return f"{str(var):6.4}{str(f1(var)):6.4}\n"


def make_header(name1: str, **keyword_parameters: str) -> str:
    if 'name2' in keyword_parameters:
        return f"""
 X     {name1}    {keyword_parameters['name2']}
-------------------
"""
    return f"""
 X     {name1}
-----------
"""
