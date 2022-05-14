# -*- coding: utf-8 -*-
"""
Created on Sat May 6:35 AM 2022

File: pwg.py
@author: David E. Mevorah
"""
import random
import string
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", "-L", type=int, dest="length", required=True)
    parser.add_argument("--number", "-N", type=int, dest="number")
    parser.add_argument("--symbols", "-S", dest="use_symbols", action="store_true")
    args = parser.parse_args()
    if not args.number:
        args.numer = 1
    return args


def random_password_generator(length, use_symbols):

    if use_symbols:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = string.ascii_letters + string.digits
    pwd = "".join(random.choice(chars) for char in range(length))

    if use_symbols:
        while len(pwd) == len(set(pwd).difference(string.punctuation)):
            pwd = "".join(random.choice(chars) for char in range(length))

    return pwd


if __name__ == "__main__":
    args = parse_arguments()
    print(args)
    for n in range(args.number):
        print(random_password_generator(args.length, args.use_symbols))

