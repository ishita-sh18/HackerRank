#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    count=0 
    key=-1 
    str1="hackerrank"
    for i in range(len(str1)):
        j=s.find(str1[i])
        if j>-1:
            count+=1 
            key=j
            s=s[j+1:]
    if count==len(str1):
        return("YES")
    else:
        return("NO")       
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
