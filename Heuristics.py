# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:53:16 2020

@author: Vivek
"""

def diagonal_distance(curr,dest,col):
    
    current_x=curr%col
    current_y=curr//col
    
    destination_x=curr%col
    destination_y=curr//col
    
    h=max(abs(current_x-destination_x),abs(current_y-destination_y))
    
    return h


def manhattan_distance(curr,dest,col):
    
    current_x=curr%col
    current_y=curr//col
    
    destination_x=curr%col
    destination_y=curr//col
    
    h=abs(current_x-destination_x)+abs(current_y-destination_y)
    
    return h

def eucledian_distance(curr,dest,col):
    
    current_x=curr%col
    current_y=curr//col
    
    destination_x=curr%col
    destination_y=curr//col
    
    h=((current_x-destination_x)**2 + (current_y-destination_y)**2)**0.5
    
    return h