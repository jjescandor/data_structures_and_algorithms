import pytest
from .hash_repeated_word import hash_repeated_word


def test_exists():
    assert hash_repeated_word


# @pytest.mark.skip("TODO")
def test_empty_string():
    sentence = ""
    assert hash_repeated_word(sentence) == None


# @pytest.mark.skip("TODO")
def test_repated_words():
    sentence = "Hi Hello Hi Hello"
    assert hash_repeated_word(sentence) == "hi"


# @pytest.mark.skip("TODO")
def test_sentence_with_symbols():
    sentence = "Sugar-free bread is unhealthy sugar is sweet"
    assert hash_repeated_word(sentence) == "is"

# @pytest.mark.skip("TODO")


def test_sentence_with_numbers():
    sentence = "I own 2 condos and 2 mortgages"
    assert hash_repeated_word(sentence) == "2"


def test_sentence_with_numbers_part_2():
    sentence = "She owns 20 cars, 1 mansion, 2 beach houses and 1 diamond ring"
    assert hash_repeated_word(sentence) == "1"
