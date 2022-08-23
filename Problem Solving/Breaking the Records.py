#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    countl=0
    countm=0
    list1=[]
    mini=scores[0]
    maxi=scores[0]
    for i in scores:
        if(i>maxi):
            maxi=i
            countm+=1 
        elif(i<mini):
            mini=i 
            countl+=1 
    list1.append(countm)
    list1.append(countl)
    return list1 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
