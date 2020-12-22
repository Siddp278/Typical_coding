import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    su = 0
    for i in range(0, len(ar)):
        su = su + ar[i]

    return su


# This the way the ide works

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
