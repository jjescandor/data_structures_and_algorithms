import pytest
try:
    from quick_sort import *
except:
    from .quick_sort import *

def test_unsorted_exists():
    assert unsorted

def test_insertion_sort_exists():
    assert quick_sort

def test_insertion_sort_exists():
    assert quick_sort

def test_reverse_sorted():
    assert quick_sort([20,18,12,8,5,-2], 0, 5) == [-2, 5, 8, 12, 18, 20]

def test_few_uniques():
    assert quick_sort([5,12,7,5,5,7], 0, 5) == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    assert quick_sort([2,3,5,7,13,11], 0, 5) == [2, 3, 5, 7, 11, 13]

def test_one_element_arr():
    assert quick_sort([1], 0, 0) == [1]

def test_empty_arr():
    assert quick_sort([], -1, -1) == []