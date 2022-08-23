#!/bin/python3
from collections import Counter 
import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    d={}
    d=Counter(arr)
    listk=list(d.keys())
    listv=list(d.values())
    val=max(listv)
    ind=listv.index(val)
    if(listv.count(val)>1):
        list1=listv[ind+1:]
        ind2=list1.index(val)+3 
        return min(listk[ind2],listk[ind])
    else:
        return listk[ind]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
