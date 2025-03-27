#!/usr/bin/env python3

import sys

def to_binary(n):
    return bin(n)[2:]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python numberToBinary.py <number>")
        sys.exit(1)    

    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Number must ne greater than or equal to 0")
            sys.exit(1)
        result = to_binary(n)
        print(result)
    except ValueError:
        print("Invalid number format")
        sys.exit(1)





    