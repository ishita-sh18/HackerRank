#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    l=[]
    count=0
    u=[]
    for i in range(65,91):
        u.append(chr(i))
    for i in range(97,123):
        l.append(chr(i))
    for (i,j) in zip(l,u):
        if i in s or j in s:
            count+=1 
    if count==26:
        return("pangram")
    else:
        return("not pangram")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
