#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(a):
    # Write your code here
    for n in range(1, a+1):
        if n % 3 == 0 and n % 5 != 0:
            print("Fizz")
        elif n%3 != 0 and n%5 == 0:
            print("Buzz")
        elif n%3 == 0 and n%5 == 0:
            print("FizzBuzz")
        else:
            print(n)

if __name__ == '__main__':
    a = int(input().strip())

    fizzBuzz(a)
