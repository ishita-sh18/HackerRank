#!/bin/python3
from collections import Counter 
import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    count=0
    odd=0
    d={}
    d=Counter(s)
    print(d)
    if len(s)%2==0:
        for i in (list(d.values())):
            if i%2==0:
                count+=1
        if count==len(list(d.values())):
            return("YES")
        else:
            return("NO")
    else:
        for i in (list(d.values())):
            if i%2==0:
                count+=1
            else:
                odd+=1 
        if odd==1 and count==len(list(d.values()))-1:
            return("YES")
        else:
            return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
