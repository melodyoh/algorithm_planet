# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:37:16 2018

@author: Administrator
"""
import random
import time
import heapq

def insertion_sort(v,p,r):
    for i in range(p+1,r):
        key = v[i]
        j = i -1
        while(key < v[j]):
            v[j+1] = v[j]
            if (j == 0):
                j -= 1
                break
            j -= 1
        v[j+1] = key
 
def get_median(V):
    half = (len(V)+1)//2
    return sorted(V)[half-1] 
#==============================================================================
# def get_median(V,p,r):
#     half = (p-r+1)//2  #若是长度(p-r)为偶, 返回第一个数为中位数，p-r=4为2，p-r=5为3
# 
#     for i in range(p+1,r):
#         key = V[i]
#         j = i -1
#         while(key < V[j]):
#             V[j+1] = V[j]
#             if (j == 0):
#                 j -= 1
#                 break
#             j -= 1
#         V[j+1] = key
#         
#     return V[p+ (half-1)] 
#==============================================================================
def partition(A,x):
    p = 0
    r = len(A)
    i = p
    
    for j in range(p,r-1):
        if A[j] == x:
            A[j],A[r-1] = A[r-1],A[j]
        if A[j] < x:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[r-1] = A[r-1],A[i]
    return i

        
    
def RS (V,p,r,k):
    
    if p+1 == r:
        return V[p]
    q = random.randint(p,r-1)
    t = q - p
    if t+1 == k:
        return V[q]
    elif t+1 < k:
        return RS(V,q+1,r,k-t-1)
    else:
        return RS(V,p,q,k)



def FindKth(V,k):
    V.sort()
    return V[k-1]
    
def FindKth3(V,k): 
    V.sort()
    return RS(V,0,len(V),5)
    

def select(V,k):
    if len(V) <= 5:
        x = get_median(V)
    else:
        num_group = len(V)//5
        B = []
        for i in range(num_group):
            B.append(get_median(V[i*5:(i+1)*5]))
        if len(V)%5 != 0:
            B.append(get_median(V[num_group*5:]))
        x = select(B,(len(B)+1)//2)
    
    t = partition(V,x)
    if t+1 == k:
        return x
    elif t+1 > k:
        return select(V[0:t],k)
    else:
        return select(V[t+1:],k-t-1)      

if __name__ == '__main__':
    num = 10000000
    k =10000
    range_b = 10000

#1. 排序之后取第k个。   
    start = time.time()
    V = []
    for i in range(num):
        V.append(random.randint(0,range_b))
    print("Time of generating the numbers",time.time()-start)
    
    start = time.time()
    print(FindKth(V,k))
    print("Time of finding the k-th",time.time()-start)
#2. 用最小优先级队列依次取出前k个。
    start = time.time()
    V = []
    for i in range(num):
        heapq.heappush(V,random.randint(0,range_b))
    print("Time of generating the numbers",time.time()-start)
    for j in range(k-1):
        heapq.heappop(V)
    print (heapq.heappop(V))
    print("Time of finding the k-th",time.time()-start)        
#3. 随机选择算法    
    start = time.time()
    V = []
    for i in range(num):
        V.append(random.randint(0,range_b))
    print("Time of generating the numbers",time.time()-start)
    
    start = time.time()
    print(FindKth3(V,k))
    print("Time of finding the k-th",time.time()-start)
#4. 最坏情况为线性时间的选择算法
    start = time.time()
    V = []
    for i in range(num):
        V.append(random.randint(0,range_b))
    print("Time of generating the numbers",time.time()-start)
    print(select(V,k))
    print("Time of finding the k-th",time.time()-start)