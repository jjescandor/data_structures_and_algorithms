import pytest
try:
    from merge_sort import *
except:
    from .merge_sort import *

def test_unsorted_exists():
    assert unsorted

def test_insertion_sort_exists():
    assert merge_sort

def test_insertion_sort_exists():
    assert merge

def test_reverse_sorted():
    assert merge_sort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]

def test_few_uniques():
    assert merge_sort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    assert merge_sort([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]

def test_one_element_arr():
    assert merge_sort([1]) == [1]

def test_empty_arr():
    assert merge_sort([]) == []