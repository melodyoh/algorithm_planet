# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:53:03 2017

@author: Administrator
"""
import numpy as np


def radix_sort(v):
    
    if len(v) == 0:
        return []
    minV = min(v)
    maxV = max(v)
    s = np.zeros(np.abs(maxV-minV)+1)
    for i in v:
        s[i-minV] += 1
    return s 
        
    
    
if __name__ == '__main__':
    A = [7, 2, 3, 2, 5, 1, 1]
    print (radix_sort(A))
    B = [-9]
    print (radix_sort(B))
    C = []
    print (radix_sort(C))