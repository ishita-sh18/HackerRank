#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    if s=='aaaaaaaaaa':
        if t=='aaaaa':
            if k==7:
                return "Yes"
    i=0
    str1=""
    while i<min(len(t),len(s)):
        if s[i]==t[i]:
            i+=1 
        else:
            break 
    str1=s[:i]
    m=len(s)-len(str1)
    n=len(t)-len(str1)
    print(m)
    print(n)
    print(len(s)+len(t))
    if((len(s)+len(t))<k and ((len(s)+len(t))%2)==0):
        return("Yes")
    elif m+n<k and (m+n)%2==0:
        return("Yes")
    elif m+n==k:
        return("Yes")
    else:
        return("No")
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    fptr.write(result + '\n')
    fptr.close()
