#!/usr/bin/env python3

import random
import string


class Scarifier:
    def __init__(self):
        self._tokens = {
            "int": Scarifier._random_id(),
            "main": Scarifier._random_id(),
            "(": Scarifier._random_id(),
            ")": Scarifier._random_id(),
            "{": Scarifier._random_id(),
            "}": Scarifier._random_id(),
            "printf": Scarifier._random_id(),
            ";": Scarifier._random_id(),
            "return": Scarifier._random_id(),
            "0": Scarifier._random_id(),  # the 0 in "return 0;"
        }

    @staticmethod
    def _define(identifier, token):
        return f"#define {identifier} {token}\n"

    @staticmethod
    def _random_id():
        return random.choice(string.ascii_letters) + str(random.randint(1, 100_000))

    def _tokens_to_identifier(self, tokens, with_newline=True):
        identifier = []

        for token in tokens:
            identifier.append(self._tokens[token])

        if with_newline:
            return " ".join(identifier) + "\n"

        return " ".join(identifier)

    def make_scary(self, text):
        source_code = "#include <stdio.h>\n\n"
        ids = []

        for letter in text:
            identifier = Scarifier._random_id()
            source_code += Scarifier._define(identifier, f'"{letter}"')

            ids.append(identifier)

        for (token, identifier) in self._tokens.items():
            source_code += Scarifier._define(identifier, token)

        source_code += "\n"

        source_code += self._tokens_to_identifier(("int", "main", "(", ")", "{"))

        source_code += self._tokens_to_identifier(("printf", "("), with_newline=False)
        source_code += " " + " ".join(ids)
        source_code += " " + self._tokens_to_identifier((")", ";"))

        source_code += self._tokens_to_identifier(("return", "0", ";"))
        source_code += self._tokens_to_identifier(("}"))

        return source_code


def main():
    what_to_say = str(input("What to say: "))
    scarifier = Scarifier()
    scary_source_code = scarifier.make_scary(what_to_say)

    with open("scary.c", "w+") as scary_file:
        scary_file.write(scary_source_code)


if __name__ == "__main__":
    main()
