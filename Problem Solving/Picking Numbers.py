#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    i=0
    j=i+1
    res=0
    count=1
    a.sort()
    while i<len(a) and j<len(a):
        if(abs(a[i]-a[j])<=1):
            count+=1
            res=max(res,count) 
            j+=1
        else:
            count=1
            i=j
            j+=1
    return res       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
