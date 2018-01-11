# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:13:44 2018

@author: Administrator
"""

def majority (v):
    c = 0
    for i in range(len(v)):
        if c == 0:
            m = v[i]
            c += 1
        elif m == v[i]:
            c += 1
        else:
            c -=1
    if (c == 0):
        return None
    else:
        c = 0
        for i in range(len(v)):
            if m == v[i]:
                c += 1
        if 2*c > len(v):
            return m
        else:
            return None


if __name__ == '__main__':
    
    v = [1,2,4,5,5,5]
    print("majority in list is",majority(v))
    