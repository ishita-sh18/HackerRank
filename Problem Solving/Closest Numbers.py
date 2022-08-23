#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    list1=[]
    arr.sort()
    res=max(arr)
    for i in range(len(arr)-1):
        res=min(res,abs(arr[i+1]-arr[i]))
    for i in range(len(arr)-1):
        if(abs(arr[i+1]-arr[i])==res):
            list1.append(arr[i])
            list1.append(arr[i+1])
    return list1 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
