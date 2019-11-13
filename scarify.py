#!/usr/bin/env python3

import string
import random
import os


def definewriter(f, token, string):
    f.write("#define %s %s\n" % (token, string))


def random_id():
    return random.choice(string.ascii_letters) + str(random.randint(1, 100000))


def main():
    say = str(input("What to say: "))

    saybit = list(say)
    identifier = ""

    ids = []

    with open("scary.c", "w+") as scaryfile:
        scaryfile.write("#include <stdio.h>\n\n")

        for bit in saybit:
            identifier = random_id()

            scaryfile.write('#define %s "%s"\n' % (identifier, bit))
            ids.append(identifier)

        intid = random_id()
        # int main() {
        # ^^^

        main = random_id()
        # int main() {
        #     ^^^^

        oparen = random_id()
        # int main() {
        #         ^

        cparen = random_id()
        # int main() {
        #          ^

        ocurly = random_id()
        # int main() {
        #            ^

        printf = random_id()
        #   printf();
        #   ^^^^^^

        semico = random_id()
        #   printf();
        #           ^

        returnid = random_id()
        #   return 0;
        #   ^^^^^^

        zero = random_id()
        #   return 0;
        #          ^

        ccurly = random_id()
        # }
        # ^

        definewriter(scaryfile, intid, "int")
        definewriter(scaryfile, main, "main")

        definewriter(scaryfile, oparen, "(")
        definewriter(scaryfile, cparen, ")")

        definewriter(scaryfile, ocurly, "{")
        definewriter(scaryfile, ccurly, "}")

        definewriter(scaryfile, printf, "printf")

        definewriter(scaryfile, semico, ";")

        definewriter(scaryfile, returnid, "return")

        definewriter(scaryfile, zero, "0")

        scaryfile.write(
            "\n{int} {main} {oparen} {cparen} {ocurly}\n".format(
                int=intid, main=main, oparen=oparen, cparen=cparen, ocurly=ocurly
            )
        )

        string = " ".join(ids)

        scaryfile.write(
            "{printf} {oparen} {string} {cparen} {semico}\n".format(
                printf=printf,
                oparen=oparen,
                string=string,
                cparen=cparen,
                semico=semico,
            )
        )

        scaryfile.write(
            "{returnid} {zero} {semico}\n".format(
                returnid=returnid, zero=zero, semico=semico
            )
        )

        scaryfile.write("{ccurly}\n".format(ccurly=ccurly))

    os.system("make scary")


if __name__ == "__main__":
    main()
