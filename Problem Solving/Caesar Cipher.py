#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    d=96
    up=64
    str1=""
    for i in s:
        if i.isalpha()==True:
            if i.islower()==True:
                if ord(i)+k>122:
                    diff=abs((ord(i)+k)-122)
                    if d+diff>122:
                        arr=d+diff
                        while arr>122:
                            arr=d+abs(arr-122)
                        str1+=chr(arr)
                    else:
                        str1+=chr(d+diff)
                else:
                    str1+=chr(ord(i)+k)
            else:
                if ord(i)+k>90:
                   sub=abs((ord(i)+k)-90)
                   if up+sub>90:
                        arr1=up+sub
                        while arr1>90:
                            arr1=up+abs(arr1-90)
                        str1+=chr(arr1)
                   else: 
                    str1+=chr(up+sub)
                else:
                    str1+=chr(ord(i)+k)
        else:
            str1+=i
    return(str1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
