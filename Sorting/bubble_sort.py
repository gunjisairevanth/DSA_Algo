#!/bin/python3

import math
import os
import random
import re
import sys


def countSwaps(n,a):
    it=0
    for i in range(n-1,0,-1):
        tmp=0
        for j in range(i):
            if a[j] > a[j+1]:
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
                it+=1
                
    print(f"Array is sorted in {it} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
                
                
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(n,a)


# Input (stdin)
# 3
# 3 2 1

# Expected Output
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3