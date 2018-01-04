# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:59:58 2018

@author: Administrator
"""

def binary_search (v, key):
    L = 0
    R = len(v)-1
    while (L <= R):
        M = L + (R-L)//2
        if v[M] == key:
            return M
        elif (key < v[M]):
            R = M-1
        elif (v[M] < key):
            L = M+1     
    return -1
    
if __name__ == '__main__':
    A = [1, 3, 5, 6, 7, 9]
    print(binary_search(A, 5))