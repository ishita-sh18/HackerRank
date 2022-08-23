#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    countd=0
    countl=0
    countu=0
    counts=0
    add=0
    d=['0','1','2','3','4','5','6','7','8','9']
    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    u=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    sc=['!','@','#','$','%','^','&','*','(',')','-','+']
    for i in str(password):
        if i in d:
            countd+=1 
        elif i in l:
            countl+=1
        elif i in u:
            countu+=1 
        elif i in sc:
            counts+=1 
    print(countd)
    print(countl)
    print(countu)
    print(counts)
    if countd<1:
        add+=1 
    if countl<1:
        add+=1 
    if countu<1:
        add+=1 
    if counts<1:
        add+=1 
    print(add)
    if n<6:
        diff=6-n
        return max(add,diff)
    else:
        return add

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
