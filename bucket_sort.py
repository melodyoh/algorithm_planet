# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 01:11:39 2018

@author: Administrator
"""
import numpy as np
import random
import time

def bucket_sort(V,E):

#V: the list to be sorted
#E: the size of each bucket

#Prepare for the buckets
    numBucket = len(V)//E+1
    B = []
    for i in range(numBucket):
        B.append([])
#put each item into the corresponding bucket
    for x in V:
        B[ int(numBucket*x) ].append(x)
#sort the items in the buckets by turns    
    for i in range(len(B)):
        B[i].sort()
        
    j = 0
    for i in range(len(B)):
        for x in B[i]:
            V[j] = x
            j += 1
    return 0


if __name__ == '__main__':
    start = time.time()
    V = []
    for i in range(5000000):
        V.append(random.uniform(0,1))
    print("Time of generating the numbers",time.time()-start)
    
    start = time.time()
#    print(V)
#    V.sort()
    bucket_sort(V,5)
#    print(V)
    print("Time of sorting",time.time()-start)
    
    
    