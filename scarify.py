#!/usr/bin/env python3

import string
import random
import os


say = str(input("What to say (at most 52 characters): "))

letters = list(say)
identifier = ''
past_ids = []

def definewriter(token, string):
    scaryfile.write("#define %s %s\n" % (token, string))

os.system("rm scary.c scary")

with open('scary.c', 'w+') as scaryfile:
    scaryfile.write("#include <stdio.h>\n\n")
    
    for letter in letters:
        identifier = random.choice(string.ascii_letters)
        
        if identifier in past_ids:
            identifier += random.choice(string.ascii_letters)
        
        scaryfile.write('#define %s "%s"\n' % (identifier, letter))
        
        past_ids.append(identifier)

    
    intid = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    # int main() {
    # ^^^
    
    main = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    # int main() {
    #     ^^^^
    
    oparen = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    # int main() {
    #         ^

    cparen = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    # int main() {
    #          ^

    ocurly = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    # int main() {
    #            ^

    printf = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    #   printf();
    #   ^^^^^^

    semico = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    #   printf();
    #           ^

    returnid = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    #   return 0;
    #   ^^^^^^

    zero = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    #   return 0;
    #          ^

    ccurly = random.choice(string.ascii_letters) + str(random.randint(1, 50))
    # }
    # ^

    
    definewriter(intid, "int")
    definewriter(main, "main")

    definewriter(oparen, "(")
    definewriter(cparen, ")")

    definewriter(ocurly, "{")
    definewriter(ccurly, "}")

    definewriter(printf, "printf")

    definewriter(semico, ";")

    definewriter(returnid, "return")

    definewriter(zero, "0")

    scaryfile.write("\n{int} {main} {oparen} {cparen} {ocurly}\n".format(
                                                            int=intid,
                                                            main=main,
                                                            oparen=oparen,
                                                            cparen=cparen,
                                                            ocurly=ocurly
                                                            ))

    string = ' '.join(past_ids)

    scaryfile.write('{printf} {oparen} {string} {cparen} {semico}\n'.format(
                                                            printf=printf,
                                                            oparen=oparen,
                                                            string=string,
                                                            cparen=cparen,
                                                            semico=semico
                                                            ))
    
    scaryfile.write("{returnid} {zero} {semico}\n".format(
                                                        returnid=returnid,
                                                        zero=zero,
                                                        semico=semico
                                                        ))

    scaryfile.write("{ccurly}\n".format(
                                        ccurly=ccurly
                                        ))

os.system("make scary")