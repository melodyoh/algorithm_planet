# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 01:24:36 2017

@author: Administrator
"""

import numpy as np



def insertion_sort(v):
    for i in range(1,len(v)):
        key = v[i]
        j = i -1
        while(key < v[j]):
            v[j+1] = v[j]
            if (j == 0):
                j -= 1
                break
            j -= 1
        v[j+1] = key
    return v



if __name__ == '__main__':
    np.random.seed(1)
    
    A = np.random.randint(0,90000,10)
    print(A)
    print(insertion_sort(A))
    
    