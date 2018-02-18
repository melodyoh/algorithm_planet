# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 01:14:28 2018

@author: Administrator
"""
import numpy as np

def countingSort(A,k):
    C = np.zeros(k+1)
    B = np.zeros(len(A))
    for x in A:
        C[x+1]+=1
    for i in range(1,len(C)):
        C[i] += C[i-1]
    for x in A:
        B[C[x]] = x
        C[x] += 1
    return B
    
    
    
    

if __name__ == '__main__':
    
    A = [2,5,3,0,2,3,0,3]
    B=countingSort(A,6)
    print (B)