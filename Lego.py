# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:10:48 2018

@author: Administrator
"""
import numpy as np
import random

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Floor(object):
    def __init__(self, n):
        self.length = 2**n
        self.floor = np.zeros((2**n,2**n), dtype = np.int)
    def get_point_state(self, Point):
        return self.floor[Point.x][Point.y]
    def cover_current_point(self, Point):
        self.floor[Point.x][Point.y] = 1
    def cover_1point_in_eachRegion(self,Covered_point_list):
        for i,j in Covered_point_list:
            self.cover_current_point(i)
            self.cover_current_point(j)
    def whether_fully_covered(self):
        print(self.floor.sum() == 2**n * 2**n)

def uncovered_to_cover(start_point, half_length):
    start_x = start_point.x
    start_y = start_point.y
    
    Covered_point_list = [[Point(start_x + half_length -1, start_y + half_length -1),
                           Point(start_x + half_length -1, start_y + half_length)],

                           [Point(start_x + half_length, start_y + half_length -1),
                            Point(start_x + half_length, start_y + half_length)]]
    return Covered_point_list
                                
        
def Lego (Floor, L, start_point, covered_point):
    if (L>0):
        half_length = L // 2
        Covered_region_x = (covered_point.x - start_point.x) // half_length
        Covered_region_y = (covered_point.y - start_point.y) // half_length        
        
        start_point_00 = start_point
        start_point_01 = Point(start_point.x, start_point.y + half_length)
        start_point_10 = Point(start_point.x + half_length, start_point.y)
        start_point_11 = Point(start_point.x + half_length, start_point.y + half_length)
        
        Covered_point_list = uncovered_to_cover(start_point, half_length)
        Covered_point_list[Covered_region_x][Covered_region_y] = covered_point
        
        Floor.cover_1point_in_eachRegion(Covered_point_list)
        
        if (half_length > 1):
#            return Floor.whether_fully_covered()
            Lego (Floor, half_length, start_point_00, Covered_point_list[0][0])
            Lego (Floor, half_length, start_point_01, Covered_point_list[0][1])
            Lego (Floor, half_length, start_point_10, Covered_point_list[1][0])
            Lego (Floor, half_length, start_point_11, Covered_point_list[1][1])
        
        
if __name__ == '__main__':
    
    np.random.seed(0)
    n = 3
    floor = Floor(n)
    
    random_x = np.random.randint(0,2**n)
    random_y = np.random.randint(0,2**n)
    
    Lego (floor, 2**n, Point(0,0), Point(random_x,random_y))
    
    print(floor.whether_fully_covered())