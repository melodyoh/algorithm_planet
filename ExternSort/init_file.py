# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:57:39 2017

@author: Administrator
"""
import numpy as np
import random
from ExternSort import ExternSort

def init_data(count, number_to_sort, unsorted_file):
    

    output_unsorted = open(unsorted_file, "w", encoding = "utf-8")
    for i in range(0,  count // number_to_sort):
        for j in range(0, number_to_sort):
            output_unsorted.write("%d " %random.randint(0,900000))
        output_unsorted.write("\n")    
    for j in range(0, count % number_to_sort):
        output_unsorted.write("%d " %random.randint(0,900000))
    output_unsorted.close()
    


if __name__ == "__main__":
    

    count = 105
    number_to_sort = 10
    unsorted_file = "unsorted_data.txt"
    sorted_file = "sorted_data.txt"

    init_data(count, number_to_sort, unsorted_file)
    ExternSort = ExternSort(unsorted_file, sorted_file, number_to_sort)
    ExternSort.sort()

    
    