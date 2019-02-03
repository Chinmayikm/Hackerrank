#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    ar.append("*")
    num_of_pairs = 0
    i = 0
    while i < n:
        if(ar[i] == ar[i+1]):
            num_of_pairs+=1
            i+=2
        else:
            i+=1
    return num_of_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()