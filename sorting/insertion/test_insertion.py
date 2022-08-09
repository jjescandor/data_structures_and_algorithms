import pytest
try:
    from insertion_sort import *
except:
    from .insertion_sort import *

def test_unsorted_exists():
    assert unsorted

def test_insertion_sort_exists():
    assert insertionSort

def test_reverse_sorted():
    assert insertionSort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]

def test_few_uniques():
    assert insertionSort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    assert insertionSort([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]

def test_one_element_arr():
    assert insertionSort([1]) == [1]

def test_empty_arr():
    assert insertionSort([]) == []
