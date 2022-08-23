#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    c=0
    for i in s:
        if(i=='a'):
            c+=1
    if(n==len(s) or n%len(s)==0):
        return c*(n//len(s))
    elif(n>len(s)):
        k=n//len(s)
        c=c*k
        k1=n%len(s)
        for i in range(0,k1):
            if s[i]=='a':
                c+=1
    else:
        c=0
        for i in range(0,n):
            if(s[i]=='a'):
                c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
