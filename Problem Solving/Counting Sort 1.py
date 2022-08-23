#!/bin/python3
from collections import Counter 
import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    d={}
    res=[]
    a=max(arr)
    for i in range(100):
        d[i]=0
    #print(d)
    for i in arr:
        d[i]+=1 
    res=list(d.values())
    return res 
    '''for k,v in list(d.items()):
        for i in range(v):
            res.append(k)
    return(res)'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
