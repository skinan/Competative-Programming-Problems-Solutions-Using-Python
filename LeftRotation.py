#!/bin/python3
# Hackerrank
# Practice>Data Structures>Arrays>Left Rotation

import math
import os
import random
import re
import sys

def leftRotation(a, n, r):
    if r % n == 0:
        return a
    else:
        d = r % n
        temp = []
        for i in range(n):
            if (i - d) >= 0:
                temp.insert(i - d, a[i])
            else:
                temp.insert(n + (i - d), a[i])
        
        return temp




if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    r = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    a_copy = leftRotation(a, n, r)
       
    for i in a_copy:
        print(i, end = " ")
