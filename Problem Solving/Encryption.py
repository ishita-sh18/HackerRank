#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    list1=[]
    str1=""
    a=re.sub(r"\s+","",s)
    print(a)
    n=math.sqrt(len(a))
    c=math.ceil(n)
    f=math.floor(n)
    fin=c 
    key=c 
    for i in range(0,len(a),fin): 
        list1.append(a[i:key])
        key+=c 
    print(list1)
    res=1000000
    for i in list1:
        length=len(i)
        res=min(res,length)
    try:
        nums=[]
        i=0
        j=0 
        while i<len(list1[0]):
            str1=""
            while j<len(list1):
                str1+=list1[j][i]
                j+=1 
            #print(str1)
            nums.append(str1)
            i+=1 
            j=0
        alpha=" ".join(nums)
        return alpha 
    except Exception as e:
        for j in list1:
            if len(j)==i:
                list1.remove(j)
        j=0 
        while i<len(list1[0]):
            str1=""
            while j<len(list1):
                str1+=list1[j][i]
                j+=1 
            #print(str1)
            nums.append(str1)
            i+=1 
            j=0
        print(nums)
        alpha=" ".join(nums)
        return alpha
        
        
        
                
        
    


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
