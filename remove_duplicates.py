# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:33:16 2017

@author: Administrator
"""


def unique(v):
    s = []
    if len(v) == 0:
        return s
    l = 0
    for r in range(len(v)):
        if (v[l] != v[r]):
            s.append(v[l])
            l=r
    s.append(v[l])
    return s




if __name__ == '__main__':
    
    A = [7, 2, 3, 2, 5, 1, 1]
    print (unique(A))
    B = [-9]
    print (unique(B))
    C = []
    print (unique(C))