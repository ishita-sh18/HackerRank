#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    count=0 
    for i in arr:
        if((i+d) in arr) and ((i+d+d) in arr):
            count+=1 
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = map(int, raw_input().rstrip().split())

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
