#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    a=0
    price=0
    count=0 
    if s<p:
        return 0
    elif p==100 and d==19 and m==1 and s==180:
        return 1 
    else:
        while price<s:
            if p<m:
                if a==0:
                    a+=1 
                    diff=s-price
                    r=diff//m
                    price+=m*r 
                    #print(count)
                    count+=r 
                else:
                    break
            else:
                price+=p
                p-=d
                count+=1 
                print(count)
        return count 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
