# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:25:21 2018

@author: Administrator
"""

import numpy as np

def maxSubSum(D,L,R):
    
    if (R-L) == 1:
        return L, R, D[L]

    else:
        M = L + (R-L)//2
        low_L, low_R, low_S = maxSubSum(D,L,M)
        high_L, high_R, high_S = maxSubSum(D,M,R)
    
        max_right_sum = D[M]
        cross_R = M+1
        right_sum = D[M]
        for i in range (M+1, R):
            right_sum += D[ i ]
            if ( right_sum > max_right_sum):
                max_right_sum  = right_sum
                cross_R = i+1
    
        max_left_sum = D[M-1]
        cross_L = M-1
        left_sum = D[M-1]
        for i in range ( M-2,-1,-1):
            left_sum += D[ i ]
            if ( left_sum > max_left_sum):
                max_left_sum  = left_sum
                cross_L= i
    
        cross_S = max_left_sum+ max_right_sum
    
        max_idx = np.argmax([low_S, high_S, cross_S])
        if max_idx == 0:
            return low_L, low_R, low_S
        elif max_idx == 1:
            return high_L, high_R, high_S
        else:
            return cross_L, cross_R, cross_S
            
def maxSubGap (P):
    D = []
    for i in range (1, len(P)):
        D.append( P[i] - P[i-1] )
    return maxSubSum(D,0,len(D))

if __name__ == '__main__':
    A = [10,11,7,10,6,8,24,23,4,6,4]
    L,R,S = maxSubGap (A)
    print("The maximum sub-Gap(from %d to %d) is : %d" %(L,R,S))    
    