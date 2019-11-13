#!/usr/bin/env python3

import string
import random
import os


def write_define(f, token, string):
    f.write(f"#define {token} {string}\n")


def random_id():
    return random.choice(string.ascii_letters) + str(random.randint(1, 100000))


def main():
    say = str(input("What to say: "))

    saybit = list(say)

    ids = []

    with open("scary.c", "w+") as scaryfile:
        scaryfile.write("#include <stdio.h>\n\n")

        for bit in saybit:
            identifier = random_id()

            scaryfile.write(f'#define {identifier} "{bit}"\n')
            ids.append(identifier)

        kw_int = random_id()
        main_function = random_id()
        left_paren = random_id()
        right_paren = random_id()
        left_brace = random_id()
        right_brace = random_id()
        printf_function = random_id()
        semicolon = random_id()
        kw_return = random_id()
        zero = random_id()  # the 0 in "return 0;"

        write_define(scaryfile, kw_int, "int")
        write_define(scaryfile, main_function, "main")

        write_define(scaryfile, left_paren, "(")
        write_define(scaryfile, right_paren, ")")

        write_define(scaryfile, left_brace, "{")
        write_define(scaryfile, right_brace, "}")

        write_define(scaryfile, printf_function, "printf")

        write_define(scaryfile, semicolon, ";")

        write_define(scaryfile, kw_return, "return")

        write_define(scaryfile, zero, "0")

        scaryfile.write(
            f"\n{kw_int} {main_function} {left_paren} {right_paren} {left_brace}\n"
        )

        string = " ".join(ids)

        scaryfile.write(
            f"{printf_function} {left_paren} {string} {right_paren} {semicolon}\n"
        )

        scaryfile.write(f"{kw_return} {zero} {semicolon}\n")

        scaryfile.write(right_brace + "\n")

    os.system("make scary")


if __name__ == "__main__":
    main()
