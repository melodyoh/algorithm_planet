# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:24:41 2018

@author: Administrator
"""

import heapq

def huffman(v):
#    n = len(v)
    f= []
    
    while (len(v)+len(f) > 1):
        if len(v) != 0:
            first = v[0]
            if len(f) == 0 or f[0] >= v[0]:
                heapq.heappop(v)
            elif f[0] < first:
                first = heapq.heappop(f)
        else:
            first = heapq.heappop(f)
        if len(v) != 0:
            second = v[0]
            if len(f) == 0 or f[0] >= v[0]:
                heapq.heappop(v)
            elif f[0] < second:
                second = heapq.heappop(f)
        else:
            second = heapq.heappop(f)
        heapq.heappush(f, first + second)
    return f

    
    
if __name__ == "__main__":
    
    v = [0.125,0.0625,0.0625,0.125,0.25,0.125,0.0625,0.125,0.0625] 
    heapq.heapify(v)
    f = huffman(v)
    
    