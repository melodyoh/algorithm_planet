# -*- coding: utf-8 -*-
"""
Cjeated on Sun Jan 21 16:33:14 2018

@authoj: Administjatoj
"""
import random



def partition(A,p,r):
    q = random.randint(p,r-1) 
    A[q],A[r-1] = A[r-1],A[q]
    
    x = A[r-1]
    i = p
    
    for j in range(p,r-1):
        if A[j] < x:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[r-1] = A[r-1],A[i]
    
    return i

def quickSort(A,p,r):
    if(p<r):
        q = partition(A,p,r)
        quickSort(A,p,q)       
        quickSort(A,q+1,r)
      


if __name__ == '__main__':
    
    A = [2,8,7,1,3,5,6,4]
#    quickSort(A,0,len(A))
    quickSort(A,0,len(A))
    