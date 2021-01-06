import math
import os
import random
import re
import sys

def decimalToBinary(n):
    return bin(n).replace("0b","")


if __name__ == '__main__':
    n = int(input())
    b = str(decimalToBinary(n))
    s = b.split('0')
    ma = []
    for i in s:
        if i != None:
            ma.append((len(i)))
            
    print(max(ma))
