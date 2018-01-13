# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 00:36:24 2018

@author: Administrator
"""

from collections import deque



class HuffmanNode(object):
    def __init__(self, weight, number,leftChild,rightChild):
        self.weight = weight
        self.number = number
        self.lChild = leftChild
        self.rChild = rightChild
        
class HuffmanTree(object):
    
    def __init__(self, P):
        self.P = P
        self.__HCode = {}
        self.size = float("inf")
    
    def HuffmanCoding(self,C):
        self.size =len(self.P)
        if self.size <= 1:
            return None
        
        data = []
        QNode = deque()
        QTree = deque()
    
        
        for i in range(0, self.size):
            data.append(HuffmanNode(self.P[i], i, None, None))
            QNode.append(data[i])
            
        index = self.size   #之前编号0~len(P), 现在len(P)开始
        
        while (len(QNode) + len(QTree) >1 ):
            Children = []
            for i in range(0,2):
                if (len(QNode) != 0):
                    Children.append(QNode[0])
                    if (len(QTree) != 0 and QTree[0].weight < QNode[0].weight):
                        Children[i] = QTree.popleft()
                    else:
                        QNode.popleft()
                else:
                    Children.append(QTree.popleft())
                    
            data.append(HuffmanNode(Children[0].weight + Children[1].weight, index, Children[0], Children[1]))
            QTree.append(data[index])
            
            index += 1
        
        self.__CodingAll(QTree[0], "")
        C = self.__HCode
        self.__printCoding()
        

    def __printCoding(self):
        string_list = []
        string_width = []
        string = ""
        l = 0
        outp = open("outputTree.txt","w",encoding="utf-8")
        for k in sorted(self.__HCode.keys(),key = lambda x:(len(x),x)):
            if len(k) > l:
                string_list.append(string)
                string_width.append(len(string))
                string = ""
                l += 1
            string = string + str(k) + ": " + str(self.__HCode[k]) + "   "
        padding_width = max(string_width)
        for s in string_list:
            outp.write(s.center(padding_width))
            outp.write("\n")

    
    def __root():
        return HuffmanNode()
    
    def __CodingAll(self,p, prefix):
        
        if (p != None):
            self.__CodingAll(p.lChild, prefix+"0")
            self.__CodingAll(p.rChild, prefix+"1")
            self.__HCode[prefix] = str(p.weight)
#            +"\t"+str(p.number)
                


if __name__ == "__main__":
        
    v = [0.125,0.0625,0.0625,0.125,0.25,0.125,0.0625,0.125,0.0625]
    
    T = HuffmanTree(P = v)
    T.HuffmanCoding(C=[])

    
    
    
    
    
    

