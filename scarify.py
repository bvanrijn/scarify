#!/usr/bin/env python3

import string
import random
import os


def define(identifier, letter):
    return f"#define {identifier} {letter}\n"


def random_id():
    return random.choice(string.ascii_letters) + str(random.randint(1, 100000))


def main():
    what_to_say = str(input("What to say: "))

    ids = []

    with open("scary.c", "w+") as scary_file:
        scary_file.write("#include <stdio.h>\n\n")

        for letter in what_to_say:
            identifier = random_id()
            scary_file.write(f'#define {identifier} "{letter}"\n')

            ids.append(identifier)

        keywords = {
            "int": random_id(),
            "main": random_id(),
            "(": random_id(),
            ")": random_id(),
            "{": random_id(),
            "}": random_id(),
            "printf": random_id(),
            ";": random_id(),
            "return": random_id(),
            "0": random_id(),  # the 0 in "return 0;"
        }

        for (keyword, identifier) in keywords:
            scary_file.write(define(keyword, identifier))

        K = keywords

        # TODO: Make a function that takes a tuple of tokens and converts them to a string
        # with their new identifier
        scary_file.write(f"\n{K['int']} {K['main']} {K['(']} {K[')']} {K['{']}\n")
        scary_file.write(f"{K['printf']} {K['(']} {' '.join(ids)} {K[')']} {K[';']}\n")
        scary_file.write(f"{K['return']} {K['0']} {K[';']}\n")
        scary_file.write(K["}"] + "\n")

    os.system("make scary")


if __name__ == "__main__":
    main()
