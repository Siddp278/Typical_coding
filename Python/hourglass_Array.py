import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    count = []
    for j in range(0, 4):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        # 0 to 3
        for i in range(0, 3):
            count1 = count1 + arr[j][i]
        k = 1
        count1 = count1 + arr[j+1][k]
        for p in range(0, 3):
            count1 = count1 + arr[j+2][p]
        count.append(count1)
        # 3 to 6
        for i in range(3, 6):
            count2 = count2 + arr[j][i]
        k = 4    
        count2 = count2 + arr[j+1][k]
        for p in range(3, 6):
            count2 = count2 + arr[j+2][p]
        count.append(count2)
        # 1 to 4
        for i in range(1, 4):
            count3 = count3 + arr[j][i]
        k = 2
        count3 = count3 + arr[j+1][k]
        for p in range(1, 4):
            count3 = count3 + arr[j+2][p]
        count.append(count3)
        # 2 to 5
        for i in range(2, 5):
            count4 = count4 + arr[j][i]
        k = 3
        count4 = count4 + arr[j+1][k]
        for p in range(2, 5):
            count4 = count4 + arr[j+2][p]
        count.append(count4)
        
    print(max(count))
        
