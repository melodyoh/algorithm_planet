# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:03:15 2018

@author: Administrator
"""


class priorityQueue (object):
    
    def __init__(self):
        #0位置为哨兵
        self.seq = [0]
        
    def __swim(self,i):
        self.seq[0] = self.seq[i]

        #与父比较，若子>父，交换，因为目标存储在0， 所以一直与0比较即可
        while (self.seq[i//2] < self.seq[0]):
#        while (self.seq[i//2] > self.seq[0]):
            #父挪到子位置
            self.seq[i] = self.seq[i//2]
            i = i//2
        
        self.seq[i] = self.seq[0]
        
        
    def __sink(self,i): 
        self.seq[0] = self.seq[i]        
        
        #最后个元素已经无效
        seq_size = len(self.seq) -1
        rChildNo = 2*i + 1
        while (rChildNo < seq_size):
            MAX = 0
            if self.seq[0] < self.seq[rChildNo]:
#            if self.seq[0] > self.seq[rChildNo]: 
                MAX = rChildNo
            if self.seq[0] < self.seq[rChildNo-1] and self.seq[rChildNo-1]>self.seq[rChildNo]:                
#            if self.seq[0] > self.seq[rChildNo-1] and self.seq[rChildNo-1]<self.seq[rChildNo]:
                MAX = rChildNo-1
            if MAX == 0:
                break
            self.seq[i]= self.seq[MAX]
            i = MAX
            rChildNo = 2*i + 1
        #特殊情况：存在左孩子且需要下沉
        if (rChildNo == seq_size and self.seq[0] < self.seq[rChildNo-1]):
#        if (rChildNo == seq_size and self.seq[i] > self.seq[rChildNo-1]):
            self.seq[i] = self.seq[rChildNo-1]
            i = rChildNo-1
        #将存储的元素赋给最终停留位置
        self.seq[i] = self.seq[0]

    def build(self,l):
        
        for i in range(len(l)):
            self.push(l[i])

    def empty(self):
        return len(self.seq) == 1
    
    def size(self):
        return len(self.seq) - 1
    
    def top(self):
        return self.seq[1]
        
    def push(self,item):
        self.seq.append(item)
        self.__swim(len(self.seq)-1)
    
    def pop(self):
        #前提非空，1位置被最小覆盖
        pop_item = self.seq[1]
        self.seq[1] = self.seq[len(self.seq)-1]
        #从1位置开始下沉
        self.__sink(1)
        self.seq.pop()
        return pop_item
        

if __name__ == '__main__':
    
    p = priorityQueue()
    p.build([13,10,1,5,7,12,4,8,9,0,27,17,3,16])
    print(p.seq)
    for i in range(p.size()):
        print(p.pop())

    
    
    