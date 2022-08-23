#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2]=="P":
        str1=s[0]+s[1]
        if str1!="12":
            a=int(str1)+12
            strn=str(a)+s[2:8]
            return (strn)
        else:
            return s[:8]
    elif s[-2]=="A":
        if int(s[0]+s[1])==12:
            a=int(s[0]+s[1])-12
            str1=(str(a)*2)+s[2:8]
            return str1 
        else:
            return s[:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
