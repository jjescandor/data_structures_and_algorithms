import pytest
try:
    from .hash_repeated_word import first_repeated_word
except:
    from hash_repeated_word import first_repeated_word


def test_exists():
    assert first_repeated_word


# @pytest.mark.skip("TODO")
def test_empty_string():
    sentence = ""
    assert first_repeated_word(sentence) == None


# @pytest.mark.skip("TODO")
def test_repated_words():
    sentence = "Hi Hello Hi Hello"
    assert first_repeated_word(sentence) == "hi"


# @pytest.mark.skip("TODO")
def test_sentence_with_symbols():
    sentence = "Sugar-free bread is unhealthy sugar is sweet"
    assert first_repeated_word(sentence) == "is"

# @pytest.mark.skip("TODO")


def test_sentence_with_numbers():
    sentence = "I own 2 condos and 2 mortgages"
    assert first_repeated_word(sentence) == "2"


def test_sentence_with_numbers_part_2():
    sentence = "She owns 20 cars, 1 mansion, 2 beach houses and 1 diamond ring"
    assert first_repeated_word(sentence) == "1"

# @pytest.mark.skip("TODO")


def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected
# @pytest.mark.skip("TODO")


def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """
    actual = first_repeated_word(txt)
    expected = "banana"
    assert actual == expected
