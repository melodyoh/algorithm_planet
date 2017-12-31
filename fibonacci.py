# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:00:45 2017

@author: Administrator
"""

import sys   
sys.setrecursionlimit(1000000)

import time
import numpy as np


#直接调用numpy.dot，大数相乘出现负数
def matrix_dot(A,B):
    return([[A[0][0]*B[0][0]+A[0][1]*B[1][0],
             A[0][0]*B[0][1]+A[0][1]*B[1][1]],
             [A[1][0]*B[0][0]+A[1][1]*B[1][0],
              A[1][0]*B[0][1]+A[1][1]*B[1][1]]])

def matrix_dot2(A,B):
    return([[A[0][0]*B[0][0]+A[0][1]*B[1][0]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0]]])



def matrix_power(A, n):
    tmp = A
    if n == 0:
        return [[1,0],[0,1]]
    else: 
        for i in range(n-1):
            tmp = matrix_dot(tmp,A)
        return tmp
        

def Fibonacci (n):
    
    if  n == 0:
        return 1,0
    else :
        Fm1,Fm0 = Fibonacci(n//2)
        if n%2 == 1:
            return Fm1 * (Fm1 + 2*Fm0), Fm1**2 + Fm0**2
        else:
            return Fm1**2 + Fm0**2, Fm0 * (2*Fm1 - Fm0)
        
def Fibonacci1 (n):
    
    A = [[1,1],[1,0]]
    if  n == 0 or n == 1:
        return [[1],[0]]
    else :
        return matrix_dot2(matrix_power(A, n),[[1],[0]])   
        
def Fibonacci2 (n):
    
    A = [[1,1],[1,0]]
    if  n == 0 or n == 1:
        return A
       
    else :
        return matrix_dot(Fibonacci2(n-1),A)

def Fibonacci3 (n):
    
    A = [0,1,1]
    if  n == 0 or n == 1:
        return A    
    else :
        A[0]=A[1]
        A[1]=A[2]
        A[2]=A[0]+A[1]
        return A
        


            


if __name__ == '__main__':
    n =  35
    
    start =time.clock()
    Fn1, Fn0 = Fibonacci(n)
    print("The %dth of Fibonancci list:%d" %(n, Fn0))
    print("test time: %.10f" %(time.clock()-start))
    
    start =time.clock()
    Fn1 = Fibonacci1(n)[1][0]
    print("The %dth of Fibonancci list:%d" %(n, Fn1))
    print("test time: %.10f" %(time.clock()-start))

    start =time.clock()
    Fn1 = Fibonacci2(n)[1][0]
    print("The %dth of Fibonancci list:%d" %(n, Fn0))
    print("test time: %.10f" %(time.clock()-start))
    
    start =time.clock()
    Fn1 = Fibonacci3(n)[1]
    print("The %dth of Fibonancci list:%d" %(n, Fn0))
    print("test time: %.10f" %(time.clock()-start))   
    