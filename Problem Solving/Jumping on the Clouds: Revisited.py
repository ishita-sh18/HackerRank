#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy=100
    i=0 
    n=len(c)
    i=(i+k)%n
    j=i
    count=0
    while i<len(c):
        if i==j and count!=0:
            break 
        if c[i]==0:
            energy-=1
            count+=1 
            i=(i+k)%n 
        else:
            energy-=3 
            count+=1 
            i=(i+k)%n
    return energy 
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
