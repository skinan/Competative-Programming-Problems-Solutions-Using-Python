#!/bin/python3
# To solve this problem , I have implemented "Prefix Sum Algorithm" here. 
# Hackerrank.com
# Practice>Data Structures>Arrays>Array Manipulation
import math
import os
import random
import re
import sys



# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l = [0]*(n + 2)
    
    for i in queries:
        l[i[0]] += i[2] 
        l[i[1]+1] -= i[2]
        
    """ Implemented "Prefix Sum Algorithm" Here """
    for i in range(1, len(l) - 1):
        l[i] = l[i - 1] + l[i]
    return max(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
