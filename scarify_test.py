import random
import subprocess
import tempfile

from scarify import Scarifier

random.seed(42)


def test_define_keyword() -> None:
    scarifier = Scarifier()

    assert scarifier._define("foo", "return") == "#define foo return\n"


def test_define_letter() -> None:
    scarifier = Scarifier()

    assert scarifier._define("foo", '"f"') == '#define foo "f"\n'


def test_random_id() -> None:
    scarifier = Scarifier()

    random_id = scarifier._random_id()
    letter = random_id[0]
    number = random_id[1:]

    assert letter.isalpha() is True
    assert number.isnumeric() is True


def test_make_scary() -> None:
    scarifier = Scarifier()
    text = "Hello, World!"
    source_code = scarifier.make_scary(text)

    with tempfile.TemporaryDirectory():
        with open("scary.c", "w+") as f:
            f.write(source_code)

        subprocess.call("gcc scary.c -o scary".split(" "))

        p = subprocess.Popen(["./scary"], stdout=subprocess.PIPE)
        p.wait()  # TODO: Fail the test if p.returncode != 0

        stdout = p.stdout.read().decode()

        assert stdout == "Hello, World!"
