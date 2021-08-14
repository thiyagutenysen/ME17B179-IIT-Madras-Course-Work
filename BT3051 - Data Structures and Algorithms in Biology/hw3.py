# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 01:02:47 2019

@author: chella
"""

maze=[[1 , 0 , 1 , 1 , 0 , 1],
[1 , 1 , 0 , 0 , 0 , 0],
[0 , 1 , 0 , 1 , 1 , 1],
[0 , 1 , 1 , 1 , 0 , 0],
[1 , 0 , 0 , 1 , 1 , 1],
[1 , 1 , 0 , 0 , 0 , 1],
[0 , 0 , 1 , 1 , 0 , 1]]

#This is perfected
class vertices:
    def __init__(self,node):
        self.node=node
        self.index=-1
        self.edge_list=[]
        self.distance = -1              # shortest distance from source node in shortest path search
        self.previous = None
    def getNeighbors(self):
        return self.edge_list
    
        
discovered=[]
exhausted=[]
ngr_list=[]
submaze=[[1 , 0 , 1 , 1 , 0 , 1],
[1 , 1 , 0 , 0 , 0 , 0],
[0 , 1 , 0 , 1 , 1 , 1],
[0 , 1 , 1 , 1 , 0 , 1],
[1 , 0 , 0 , 1 , 1 , 1],
[1 , 1 , 0 , 0 , 0 , 1],
[0 , 0 , 1 , 1 , 0 , 1]]

def iterate(ngr_list):
    cool=[]
    for i in ngr_list:
        print(i.node[0],i.node[1])
        if(ngr_list!=[]):
            if i.node[0]<=5 and i.node[1]<=5:
                print(1)
                if maze[i.node[0]+1][i.node[1]]==1 and (i.node[0]+1,i.node[1]) in discovered:
                    print(1)
                    i.edge_list.append(submaze[i.node[0]+1][i.node[1]])
                elif maze[i.node[0]+1][i.node[1]]==1 and(i.node[0]+1,i.node[1]) not in discovered:
                    print(6)
                    address=vertices((i.node[0]+1,i.node[1]))
                    cool.append(address)
                    i.edge_list.append(address)
                    submaze[i.node[0]+1][i.node[1]]=address
                    #discovered.append((i.node[0]+1,i.node[1]))
                    print(1)
            if i.node[0]>0 and i.node[1]<=5:
                if maze[i.node[0]-1][i.node[1]]==1 and (i.node[0]-1,i.node[1]) in discovered:
                    print(2)
                    i.edge_list.append(submaze[i.node[0]-1][i.node[1]])
                elif maze[i.node[0]-1][i.node[1]]==1 and(i.node[0]-1,i.node[1]) not in discovered:
                    print(2)
                    address=vertices((i.node[0]-1,i.node[1]))
                    cool.append(address)
                    i.edge_list.append(address)
                    submaze[i.node[0]-1][i.node[1]]=address
                    #discovered.append((i.node[0]-1,i.node[1]))
            if i.node[0]<=6 and i.node[1]<=4:
                if maze[i.node[0]][i.node[1]+1]==1 and (i.node[0],i.node[1]+1) in discovered:
                    i.edge_list.append(submaze[i.node[0]][i.node[1]+1])
                elif maze[i.node[0]][i.node[1]+1]==1 and(i.node[0],i.node[1]+1) not in discovered:
                    print(3)
                    address=vertices((i.node[0],i.node[1]+1))
                    cool.append(address)
                    i.edge_list.append(address)
                    submaze[i.node[0]][i.node[1]+1]=address
                    #discovered.append((i.node[0],i.node[1]+1))
            if i.node[0]<=6 and i.node[1]>0:
                if maze[i.node[0]][i.node[1]-1]==1 and (i.node[0],i.node[1]-1) in discovered:
                    print(9)
                    i.edge_list.append(submaze[i.node[0]][i.node[1]-1])
                elif maze[i.node[0]][i.node[1]-1]==1 and(i.node[0],i.node[1]-1) not in discovered:
                    print(4)          
                    address=vertices((i.node[0],i.node[1]-1))
                    cool.append(address)
                    i.edge_list.append(address)
                    submaze[i.node[0]][i.node[1]-1]=address
                    #discovered.append((i.node[0],i.node[1]-1))
        else:
            break
        if (i.node[0],i.node[1]) not in discovered:
            exhausted.append(i)
            discovered.append((i.node[0],i.node[1]))
            print(discovered)
    if (cool==[]):
        return
    else:
        iterate(cool)
            
def create_graph(maze):
    for i, x in enumerate(maze):
        for j, val in enumerate(x):
            if maze[i][j]==1 and (i,j) not in discovered:
                print("done")
                ngr_list=[]
                address=vertices((i,j))
                submaze[i][j]=address
                ngr_list.append(address)
                iterate(ngr_list)
                print("done")
                
                
create_graph(maze)
print(submaze)
for i,j in enumerate(exhausted):
    j.index=i
    print(j.index,j.node,j.edge_list)

visit=[0]*len(exhausted)
ccnum=[0]*len(exhausted)
def explore(v,cc):
    print(v.index,v.node)
    visit[v.index]=1
    ccnum[v.index]=cc
    for j in v.edge_list:
        
        if visit[j.index]==0:
            
            explore(j,cc)
    
def DFS(exhausted):
    cc=1
    for val in exhausted:
        print("*")
        if visit[val.index]==0:
            explore(val,cc)
            cc+=1
DFS(exhausted)
print(ccnum)

dist=[0]*len(exhausted)
previous=[0]*len(exhausted)
def min_dist(q):
    k=0
    k_index=0
    q_index=0
    for j,i in enumerate(q):
        if dist[i.index]<k:
            k=dist[i.index]
            k_index=i.index
            q_index=j
    return k_index,q_index
def dijkstra(graph,source):
    for v in graph:
        dist[v.index]=-1
        previous[v.index]=0
    dist[source.index]=0
    q=graph.copy()
    while q!=[]:
        index,q_index= min_dist(q)
        q.pop(q_index)
        for i in graph[index].edge_list:
                alt=dist[index]+1
                if alt<dist[i.index]:
                    
                    dist[i.index]=alt
                    previous[i.index]=graph[index]
    print(dist)
dijkstra(exhausted,exhausted[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        