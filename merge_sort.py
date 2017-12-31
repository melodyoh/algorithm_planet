# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 01:07:52 2017

@author: Administrator
"""

import numpy as np
import time

def merge(V,L,M,R):
    leftList = np.append(V[L:M],float("inf"))
    rightList = np.append(V[M:R],float("inf"))
    
    leftIndex = 0
    rightIndex = 0
    
    for i in range(L,R):
        if (leftList[leftIndex] < rightList[rightIndex]):
            V[i] = leftList[leftIndex]
            leftIndex +=1
        else:
            V[i] = rightList[rightIndex]
            rightIndex +=1            


def merge_sort(V,L,R):
    if (L< R-1):
        M = L + (R-L)//2
        merge_sort(V,L,M)
        merge_sort(V,M,R)
        merge(V,L,M,R)
        
if __name__ == "__main__":
    
    numList = np.random.randint(0,900,900000)
    start = time.clock()
#    print(numList)

    merge_sort(numList,0,len(numList))
    print (time.clock()-start)
#    print(numList)    