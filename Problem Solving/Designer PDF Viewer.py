#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    d={}
    i=97
    j=0
    list1=[]
    while i<=122:
        d[chr(i)]=j
        i+=1
        j+=1 
    print(d)
    for i in word:
        val=d[i]
        list1.append(h[val])
    area=len(word)*max(list1)
    return area 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
