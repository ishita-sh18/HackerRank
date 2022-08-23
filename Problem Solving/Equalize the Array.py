#!/bin/python
from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    d={}
    d=Counter(arr)
    listv=list(d.values())
    max1=max(listv)
    listv.remove(max1)
    return sum(listv)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
