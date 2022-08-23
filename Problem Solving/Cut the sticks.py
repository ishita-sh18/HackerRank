#!/bin/python3
from collections import Counter 
import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    d={}
    j=0
    a=[]
    a.append(len(arr))
    arr.sort()
    d=Counter(arr)
    for k,v in list(d.items()):
        j+=v
        if len(arr)-j!=0:
            a.append(len(arr)-j)
    return a
       
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
