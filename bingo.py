#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from random import choice, sample

def main():
    source = open("gjestebingo.txt", "r")
    pre = open("prefix.txt", "r")
    post = open("postfix.txt", "r")
    image = open("image.txt", "r")

    f = open("testbingo.tex", "w+")

    for i in pre.readlines():
        f.write(i)


    fl = source.readlines()
    a = []

    for i in range(5):

        f.write(pre.read())
        if i == 0:
            random_sample = random.sample(fl, 5)
        else:
            l3 = [x for x in fl if x not in a]
            random_sample = random.sample(l3, 5)

        a.extend(random_sample)

        for sample in random_sample:
            hei = sample + "&";
            if sample == random_sample[-1]:
                hei = sample + "\\\\\hline\n"
            
            elif sample == random_sample[2] and i == 2:
                hei =image.read()
            

            f.write(hei)
    f.write(post.read())

if __name__ == "__main__":
    main()
