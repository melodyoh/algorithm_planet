# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:50:33 2017

@author: Administrator
"""
import numpy as np 

class ExternSort(object):
    def __init__ (self, unsorted_file, sorted_file, number_to_sort):
        
        self.number_to_sort = number_to_sort
        self.unsorted_file = unsorted_file
        self.sorted_file = sorted_file

    def memory_sort (self):
        file_count = 0
        for line in open(self.unsorted_file,"r", encoding = "utf-8"):
            array = line.split()
            array = list(map(int, array))
            array.sort()
            temp_file = "temp_%d.txt" %file_count
            output_temp=open(temp_file, "w", encoding = "utf-8")           
            #写入文件
            for j in range(0,len(array)):
                output_temp.write("%d\n" %array[j])
            output_temp.close()            
            file_count +=1
        
        del array
        return file_count

#==============================================================================
#         file_count = 0
#         i = 0
#         array = []
#         input_temp = open(self.unsorted_file,"r", encoding = "utf-8")
#         line = input_temp.readline()
# 
#         while line:
#             for i in range(0,self.number_to_sort):
#                 if line != '':
#                     array.append(int(line))
#                 line = input_temp.readline()
#             array.sort()
#             file_count +=1
#             i = 0
#             array = []
#==============================================================================
     
    def merge_sort(self,file_count):
        unsorted_data = []
        file_openlist = []
        file_list = np.arange(0,file_count)
        finished_file_count = 0
        output_file=open(self.sorted_file, "w", encoding = "utf-8") 
        
        for i in range(0,file_count):
            temp_file = "temp_%d.txt" %i
            file_openlist.append(open(temp_file,"r", encoding = "utf-8"))
            line = file_openlist[i].readline()
            unsorted_data.append(int(line))
            
        while (finished_file_count < file_count-1):
            min_idx = np.argmin(unsorted_data)
            output_file.write("%d " %np.min(unsorted_data))
            
            line = file_openlist[min_idx].readline()
            if line != '':
                unsorted_data[min_idx] = int(line)
            else:
                unsorted_data[min_idx] = float("inf")
                file_openlist[min_idx].close()
                file_list[min_idx] = -1
                finished_file_count += 1
        
        unfinished_idx = np.argmax(file_list)
        output_file.write("%d " %unsorted_data[unfinished_idx])
        
        line = file_openlist[unfinished_idx].readline()
        while (line != ''):
            output_file.write("%d " %int(line))
            line = file_openlist[unfinished_idx].readline()
            
        file_openlist[unfinished_idx].close()
        output_file.close()
        
    def sort(self):
        file_count = self.memory_sort()
        self.merge_sort(file_count)
        
        
        
            
            
            
        
    