#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year<=1917:
        if year%4==0:
            str1=("12.09.")
            str1+=str(year)
            return(str1)
        else:
            str1=("13.09.")
            str1+=str(year)
            return(str1)
    elif year==1918:
        str1="26.09.1918"
        return str1
    elif year>=1919:
        if year%400==0 or (year%4==0 and year%100!=0):
            str1=("12.09.")
            str1+=str(year)
            return(str1)
        else:
            str1=("13.09.")
            str1+=str(year)
            return(str1)
        
    
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
