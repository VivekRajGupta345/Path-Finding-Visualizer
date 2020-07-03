# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:53:16 2020

@author: Vivek
"""

class heap_node:
    def __init__(self):
        self.key=None
        self.val=float("inf")
        self.parent=None

class min_heap:
    def __init__(self):
        self.heap=[]
        self.mapp={}
        
    def isempty(self):
        
        if len(self.heap)==0:
            return True
        else:
            return False
    
    def get_parent(self,i):
        
        return (i-1)//2
    
    def get_leftchild(self,i):
        
        return 2*i+1
    
    def get_rightchild(self,i):
        
        return 2*i+2
    
    def heapify_up(self,pos):
        
        i=pos
        
        while(self.get_parent(i)>=0):
            
            j=self.get_parent(i)
            #print(j,end="*")
            
            if self.heap[i].val<self.heap[j].val:
                
                self.mapp[self.heap[i].key]=j
                self.mapp[self.heap[j].key]=i
                
                self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
                i=j
            else:
                break
    
    
    
    def push(self,keys,value,parents):
        
        elem=heap_node()
        elem.val=value
        elem.key=keys
        elem.parent=parents
        
        self.heap.append(elem)
        self.mapp[elem.key]=len(self.heap)-1
        self.heapify_up(len(self.heap)-1)
    
    def peek(self):
        return self.heap[0]
    
    def heapify_down(self):
        i=0
        left_child=self.get_leftchild(i)
        right_child=self.get_rightchild(i)
        
        while(left_child<len(self.heap)):#due to property of heap that it fills in left to right top to bottom
            
            if right_child<len(self.heap):
                
                if self.heap[left_child].val<self.heap[right_child].val:
                    if self.heap[i].val>self.heap[left_child].val:
                        self.mapp[self.heap[i].key]=left_child
                        self.mapp[self.heap[left_child].key]=i
                        self.heap[i],self.heap[left_child]=self.heap[left_child],self.heap[i]
                        i=left_child
                        
                    else:
                        break
                else:
                    if self.heap[i].val>self.heap[right_child].val:
                        self.mapp[self.heap[i].key]=right_child
                        self.mapp[self.heap[right_child].key]=i
                        self.heap[i],self.heap[right_child]=self.heap[right_child],self.heap[i]
                        i=right_child
                    else:
                        break
            else:
                if self.heap[i].val>self.heap[left_child].val:
                    self.mapp[self.heap[i].key]=left_child
                    self.mapp[self.heap[left_child].key]=i
                    self.heap[i],self.heap[left_child]=self.heap[left_child],self.heap[i]
                    i=left_child
                else:
                    break
            
            left_child=self.get_leftchild(i) 
            right_child=self.get_rightchild(i)
                
    def extract_min(self):
        
        if len(self.heap)>0:
        
            self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
            self.mapp[self.heap[0].key]=0
            temp=self.heap.pop()
            self.mapp[temp.key]=None
            
            self.heapify_down()
            return temp
        else:
            print("Error")
    
    def get_val(self,key):
        
        if self.mapp.get(key)!=None:
            return self.heap[self.mapp[key]].val
        else:
            return None
    
    def contains(self,key):
        
        if self.mapp.get(key)==None:
            return None
        else:
            return True
    
    def decrease_key(self,key,new_val,new_parent):
        pos=self.mapp[key]
        self.heap[pos].val=new_val
        self.heap[pos].parent=new_parent
        self.heapify_up(pos)

