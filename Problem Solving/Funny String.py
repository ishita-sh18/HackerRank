#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    a=s[::-1]
    list1=[]
    list2=[]
    for i in range(len(a)-1):
        list1.append(abs(ord(s[i])-ord(s[i+1])))
    for j in range(len(a)-1):
        list2.append(abs(ord(a[j])-ord(a[j+1])))
    if list1==list2:
        return("Funny")
    else:
        return("Not Funny")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()