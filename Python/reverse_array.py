import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    # The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
    arr = list(map(int, input().rstrip().split()))
    str1 = str(arr[n - 1])
    for i in range(1,n):
        str1 = str1 + " " + str(arr[len(arr) - i - 1])
    print(str1)
