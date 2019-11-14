import random

from scarify import Scarifier

random.seed(42)


def test_define_keyword():
    scarifier = Scarifier()

    assert scarifier._define("foo", "return") == "#define foo return\n"


def test_define_letter():
    scarifier = Scarifier()

    assert scarifier._define("foo", '"f"') == '#define foo "f"\n'


def test_random_id():
    scarifier = Scarifier()

    random_id = scarifier._random_id()
    letter = random_id[0]
    number = random_id[1:]

    assert letter.isalpha() is True
    assert number.isnumeric() is True
