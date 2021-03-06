# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:53:16 2020

@author: Vivek
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivyoav.delayed import delayable
from collections import deque
from Heap import min_heap
from Heuristics import eucledian_distance


Window.fullscreen = "auto"
#Window.size=[400,400]

class About_Popup(Popup):
    pass

class MyWidget(GridLayout):
    
    def on_touch_move(self,touch):
        if self.ids["Start"].disabled!=True:
            for i in self.buck:
                
                if i.collide_point(touch.pos[0],touch.pos[1]):
                    
                    i.background_color=[0,0,0,1]
                    i.disabled=True
                    break

    def get_button_number(self,x,y):
        
        return self.col*y+x
    
    
    
    def touch_down(self,butt):
        if self.ids["Start"].disabled!=True:
            butt.background_color=[0,0,0,1]
            butt.disabled=True       
        
            
            
    def create_grid(self):
        
        self.buck=[]
        self.source="NA"
        self.dest="NA"
        
        wind_size=Window.size
        
        num_buttons=int((wind_size[0]*wind_size[1]*0.9)/529)
        row=int(num_buttons**0.5)
        col=num_buttons//row
        
        self.col=col
        self.row=row
        self.ids["grid2"].rows=row
        self.ids["grid2"].cols=col
        
        
        for i in range (0,row*col):
            
            butt=Button()
            butt.bind(on_press = self.touch_down)
            self.ids["grid2"].add_widget(butt)
            self.buck.append(butt)
        
        
      
    def Input(self):
        
        msg1=self.ids["srcxinp"].text
        if msg1!="":
            msg1=str(int(msg1))
        msg2=self.ids["srcyinp"].text
        if msg2!="":
            msg2=str(int(msg2))
        msg3=self.ids["destxinp"].text
        if msg3!="":
            msg3=str(int(msg3))
        msg4=self.ids["destyinp"].text
        if msg4!="":
            msg4=str(int(msg4))
        
       
        
        if msg1=="" :
            msg1="NA"
        if msg2=="" :
            msg2="NA" 
        if msg3=="" :
            msg3="NA"
        if msg4=="":
            msg4="NA"

        
        ###########SRC-X#####################
        if self.ids["srcxinp"].focus!=True:
            if msg1!="NA":
                if int(msg1)<0 or int(msg1)>self.col-1 :
                  warning_row=Button(text="Please Select X cordinates between 0 and "+str(self.col-1),disabled=True)
                  popup=Popup(title="",content=warning_row,size_hint=[0.3,0.3])
                  self.ids["dropdown_srcX"].dismiss()
                  msg1="NA"
                  self.ids["srcxinp"].text=""
                  popup.open()
                else:
                
                    self.ids["SourceX"].text="Src-x: "+msg1
                    self.ids["dropdown_srcX"].dismiss()
            
        #############SRC-y####################
        if self.ids["srcyinp"].focus!=True:
            if msg2!="NA":
                if int(msg2)<0 or int(msg2)>self.row-1 :
                    warning_col=Button(text="Please Select Y cordinates between 0 and "+str(self.row-1),disabled=True)
                    popup=Popup(title="",content=warning_col,size_hint=[0.3,0.3])
                    self.ids["dropdown_srcY"].dismiss()
                    msg2="NA"
                    self.ids["srcyinp"].text=""
                    popup.open()
                else:
                    self.ids["SourceY"].text="Src-y: "+msg2
                    self.ids["dropdown_srcY"].dismiss()
                
        #############Dest-x####################
        if self.ids["destxinp"].focus!=True:
            if msg3!="NA":
                if int(msg3)<0 or int(msg3)>self.col-1:
                    warning_row=Button(text="Please Select X cordinates between 0 and "+str(self.col-1),disabled=True)
                    popup=Popup(title="",content=warning_row,size_hint=[0.3,0.3])
                    self.ids["dropdown_destX"].dismiss()
                    msg3="NA"
                    self.ids["destxinp"].text=""
                    popup.open()
                else:
    
                    self.ids["DestX"].text="Dest-x: "+msg3
                    self.ids["dropdown_destX"].dismiss()
            
        #############Dest-y####################
        if self.ids["destyinp"].focus!=True:
            if msg4!="NA":
                if int(msg4)<0 or int(msg4)>self.row -1:
                    warning_col=Button(text="Please Select Y cordinates between 0 and "+str(self.row-1),disabled=True)
                    popup=Popup(title="",content=warning_col,size_hint=[0.3,0.3])
                    self.ids["dropdown_destY"].dismiss()
                    msg4="NA"
                    self.ids["destyinp"].text=""
                    popup.open()
                else:
                    self.ids["DestY"].text="Dest-y: "+msg4
                    self.ids["dropdown_destY"].dismiss()
            
        if msg1!="NA" and msg2!="NA":
            
            s_x=int(msg1)
            s_y=int(msg2)
            
            
            X=self.get_button_number(s_x,s_y)
            
            if self.source!="NA":
                
                self.buck[self.source].text=""
                self.buck[self.source].bold=False
                self.buck[self.source].background_color=[1,1,1,1]
                
            self.buck[X].text="S"
            self.buck[X].bold=True
            self.buck[X].background_color=[1,1,0,1]            
            self.source=X
        
            
        if  msg3!="NA" and msg4!="NA":
            
           
            d_x=int(msg3)
            d_y=int(msg4)
                    
            Y=self.get_button_number(d_x,d_y)
            
            if self.dest!="NA":
                
                self.buck[self.dest].text=""
                self.buck[self.dest].bold=False
                self.buck[self.dest].background_color=[1,1,1,1]
            
            self.buck[Y].text="D"
            self.buck[Y].bold=True         
            self.buck[Y].background_color=[1,1,0,1]
            self.dest=Y
            
                           
    def reset(self):
        
        for i in self.buck:
            
            i.bold=False
            i.background_color=[1,1,1,1]
            i.disabled=False
            i.text=""
        
        self.ids["srcxinp"].text=""
        self.ids["srcyinp"].text=""
        self.ids["destxinp"].text=""
        self.ids["destyinp"].text=""
        self.ids["AlgoButton"].text="Algo"
        self.source="NA"
        self.dest="NA"
        
        self.ids["SourceX"].text="Src-x: NA"
        self.ids["SourceY"].text="Src-y: NA"
        self.ids["DestX"].text="Dest-x: NA"
        self.ids["DestY"].text="Dest-y: NA"
        
        self.Input()
    
    def about(self):
        
        popup=About_Popup()
        
        #popup=Popup(title="About",content=content,size_hint=[0.5,0.5])
        popup.open()
    
    def close(self):
        Window.close()
        
    def clean(self):
        
        for i in self.buck:
            
            if i.text=="S" or i.text=="D" :
                i.background_color=[1,1,0,1]
            elif i.background_color==[0,0,0,1]:
                pass
            else:
                i.background_color=[1,1,1,1]
            
    def movement(self,curr):
        
        arr=[]
        
        if (curr+1)%self.col==0:
            
            arr.append(curr-1)
            arr.append(curr+self.col)
            arr.append(curr-self.col)        
            arr.append(curr-self.col-1)
            arr.append(curr+self.col-1)
        elif curr%self.col==0:
            arr.append(curr+1)
            arr.append(curr+self.col)
            arr.append(curr-self.col)
            arr.append(curr-self.col+1)
            arr.append(curr+self.col+1)
        else:  
            arr.append(curr+1)
            arr.append(curr-1)
            arr.append(curr+self.col)
            arr.append(curr-self.col)        
            arr.append(curr-self.col+1)
            arr.append(curr-self.col-1)
            arr.append(curr+self.col+1)
            arr.append(curr+self.col-1)
        
        return arr
    
    def is_valid(self,curr):
        if curr<0 or curr>(self.row*self.col)-1 or self.buck[curr].disabled==True:
            return False
        else:
            return True
    
   
    def DFS(self,curr,dest,Flag,visited,path,source,traversed):
        if visited.get(curr):
            return None
        
        elif not self.is_valid(curr):
            return None
        
        elif Flag[0]!=True:
            
            visited[curr]=True
            path.append(curr)
            traversed.append(curr)
            
            if curr==dest:
                Flag[0]=True
                
                return None
            else:
            
                moves=self.movement(curr)
                
                for i in moves:
                    
                    self.DFS(i,dest,Flag,visited,path,source,traversed)
                
                if Flag[0]!=True:
                    
                    path.pop()
                    
    def BFS(self,source,dest,Flag,path,traversed):
        
        queue=deque()
        
        if self.is_valid(source):#edge case
            queue.append([source])
            visited={}
            while(queue):
                
                temp_path=queue.popleft()
                
                curr=temp_path[-1]
                
                visited[curr]=True
                traversed.append(curr)
                
                if curr==dest:
                    Flag[0]=True
                    for i in temp_path:
                        path.append(i)
                    break
                    
                else:                
                    
                    moves=self.movement(curr)
                    
                    for i in moves:
                        
                        if self.is_valid(i):
                            
                            if visited.get(i)==None:
                                
                                queue.append(temp_path+[i])
                                visited[i]=True
                            
                
    def IDS_dfs(self,arr,depth,curr,dest,visited,queue,path_list,Flag,path,traversed):
        
        if visited.get(curr)==True or Flag[0]==True or not self.is_valid(curr):
            return 
       
        elif depth==0:
            visited[curr]=True
            traversed.append(curr)
            arr.append(curr)
            
            moves=self.movement(curr)
            
            if curr==dest:
                for j in arr:
                    path.append(j)
                Flag[0]=True
                return
            
            for i in moves:
                if visited.get(i)==None and self.is_valid(i):
                    queue.append(i)
                    path_list.append(arr[:])
                    
                
            arr.pop()
        else:
            visited[curr]=True
            arr.append(curr)
            traversed.append(curr)
            if curr==dest:
                for j in arr:
                    path.append(j)
                Flag[0]=True
                return
            
            moves=self.movement(curr)
            for i in moves:
                
                self.IDS_dfs(arr,depth-1,i,dest,visited,queue,path_list,Flag,path,traversed)
            
            arr.pop()
            
            
            
            
    def IDS_bfs(self,source,dest,Flag,max_depth,path,traversed):
        
        visited={}
        queue=deque()
        queue.append(source)
        path_list=deque()
        path_list.append([])
        
        if not self.is_valid(source):###edge case
            return 
        else:
            while(queue):
                
                if  Flag[0]==True:
                    break
                
                temp=queue.popleft()
                
                arr=path_list.popleft()            
                
                
                self.IDS_dfs(arr,max_depth,temp,dest,visited,queue,path_list,Flag,path,traversed)
            
    
    def Dijkstras(self,source,Flag,dest,traversed,path):
        
        if self.is_valid(source):
            
            short_path={} #stores button number as key and its parent as value
            heap=min_heap()
            
            for i in range(0,self.row*self.col):
                if self.is_valid(i):
                    heap.push(i,float("infinity"),None)
            
            heap.decrease_key(source,0,None)
            
            while(not heap.isempty()):
                
                node=heap.extract_min()
                if node.val<float("inf"):
                    traversed.append(node.key)
                    
                    short_path[node.key]=node.parent
                    
                    moves=self.movement(node.key)
                    
                    for i in moves:
                        
                        if self.is_valid(i) and heap.contains(i):
                        
                            if node.val+1<heap.get_val(i):
                                
                                heap.decrease_key(i,node.val+1,node.key)
               
            if short_path.get(dest)!=None:
                Flag[0]=True
                temp=short_path.get(dest)
                stack=[]
                stack.append(dest)
                
                while(temp):
                    stack.append(temp)
                    temp=short_path.get(temp)
                
                while(stack):
                    
                    temp=stack.pop()
                    path.append(temp)
                    
                    
    def Best_First(self,source,dest,Flag,traversed,path):
        
        if self.is_valid(source):
            
            shortest_path={} #stores button number as key and its parent as value
            
            heap=min_heap()
            
            for i in range(0,self.row*self.col):
                
                if self.is_valid(i):
                    heap.push(i,float("inf"),None)
            
            source_cost=eucledian_distance(source,dest,self.col)
            
            heap.decrease_key(source,source_cost,None)
            
            while(not heap.isempty()):
                
                node=heap.extract_min()
                
                if node.val<float("inf"):
                    
                    traversed.append(node.key)
                    shortest_path[node.key]=node.parent
                    
                    if node.key==dest:
                        Flag[0]=True
                        break

                    moves=self.movement(node.key)
                    
                    for i in moves:
                        
                        if self.is_valid(i) and heap.contains(i) :
                           
                            cost=eucledian_distance(i,dest,self.col)
                            
                            if cost<heap.get_val(i):
                                
                                heap.decrease_key(i,cost,node.key)

            if Flag[0]==True:
                
                stack=[]
                
                stack.append(dest)
                
                temp=shortest_path.get(dest)
                
                while(temp):
                    
                    stack.append(temp)
                    
                    temp=shortest_path.get(temp)
                
                while(stack):
                    
                    temp=stack.pop()
                    path.append(temp)
                    
        
    def A_star(self,source,dest,Flag,traversed,path):
        
        if self.is_valid(source):
            
            shortest_path={} #stores button number as key and its parent as value
            g={} #distance travelled from source to key
            heap=min_heap()
            
            for i in range(0,self.row*self.col):
                
                if self.is_valid(i):
                    heap.push(i,float("inf"),None)
            
            source_cost=eucledian_distance(source,dest,self.col) + 0
            
            heap.decrease_key(source,source_cost,None)
            g[source]=0
            
            while(not heap.isempty()):
                
                node=heap.extract_min()
                
                if node.val<float("inf"):
                    
                    traversed.append(node.key)
                    shortest_path[node.key]=node.parent
                    
                    if node.key==dest:
                        Flag[0]=True
                        break

                    moves=self.movement(node.key)
                    
                    for i in moves:
                        
                        if self.is_valid(i) and heap.contains(i) :
                           
                            cost=eucledian_distance(i,dest,self.col)+ g[node.key]
                            
                            g[i]=g[node.key]+1
                            
                            if cost<heap.get_val(i):
                                
                                heap.decrease_key(i,cost,node.key)

            if Flag[0]==True:
                
                stack=[]
                
                stack.append(dest)
                
                temp=shortest_path.get(dest)
                
                while(temp):
                    
                    stack.append(temp)
                    
                    temp=shortest_path.get(temp)
                
                while(stack):
                    
                    temp=stack.pop()
                    path.append(temp)
                    
    
    
    @delayable 
    def start(self):
        
        if self.source=="NA" or self.dest=="NA":
            content=Button(text="Please enter the Source and Destination cordinates",disabled=True)
            popup = Popup(title="",content=content,size_hint=[0.3,0.3])
            popup.open()
            
        elif self.ids["AlgoButton"].text=="Algo":
            
            content=Button(text="Please select the Algorithm to be used",disabled=True)
            popup = Popup(title="",content=content,size_hint=[0.3,0.3])
            popup.open()
            
        else:
            self.clean()                    
            path=[]
            Flag=[False]
            source=self.source
            dest=self.dest
            traversed=[]
            
            self.ids["AlgoButton"].disabled=True
            self.ids["Start"].disabled=True
            self.ids["Reset"].disabled=True
            self.ids["SourceX"].disabled=True
            self.ids["SourceY"].disabled=True
            self.ids["DestX"].disabled=True
            self.ids["DestY"].disabled=True
            self.ids["About"].disabled=True
            
            if self.ids["AlgoButton"].text=="BFS":
                self.BFS(source,dest,Flag,path,traversed)
                
            elif self.ids["AlgoButton"].text=="DFS":
                visited={}
                self.DFS(source,dest,Flag,visited,path,source,traversed)
            
            elif self.ids["AlgoButton"].text=="IDS":
                max_depth=4
                self.IDS_bfs(source,dest,Flag,max_depth,path,traversed)
                
            elif self.ids["AlgoButton"].text=="Dijkstra's":
                
                self.Dijkstras(source,Flag,dest,traversed,path)
                
            elif self.ids["AlgoButton"].text=="Greedy-Best First":
                
                self.Best_First(source,dest,Flag,traversed,path)
                
            elif self.ids["AlgoButton"].text=="A*":
                
                self.A_star(source,dest,Flag,traversed,path)
            
            for i in traversed:
                yield 0.1
                
                self.buck[i].background_color=[0.888026005753999,0.44633413667676225,0.17094569623391598,1]
                
                
            
            if Flag[0]==True:
            
                for i in path:                  
                   
                   self.buck[i].background_color=[0.21903453537169115,0.6715567266291189,0.4497686499711627,1]
                   temp=self.buck[i].text
                   self.buck[i].text="*"
                   yield 0.3
                   self.buck[i].text=temp
            else:
                
                butt=Button(text="Destination cannot be reached.",disabled=True)
                
                popup=Popup(content=butt,size_hint=[0.3,0.3])      
                popup.open()
                 
            
            self.ids["AlgoButton"].disabled=False
            self.ids["Start"].disabled=False
            self.ids["Reset"].disabled=False
            self.ids["SourceX"].disabled=False
            self.ids["SourceY"].disabled=False
            self.ids["DestX"].disabled=False
            self.ids["DestY"].disabled=False
            self.ids["About"].disabled=False

                         
        
    

class WidgetsApp(App):
          
            
           
    def build(self):
        root=MyWidget()
        
        root.create_grid()
        
        return root
    
    
if __name__=="__main__":
    WidgetsApp().run()