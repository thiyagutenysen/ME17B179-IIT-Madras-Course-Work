# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:37:40 2019

@author: chella
"""

maze=[[1 , 0 , 1 , 1 , 0 , 1],
[1 , 1 , 0 , 0 , 0 , 0],
[0 , 1 , 0 , 1 , 1 , 1],
[0 , 1 , 1 , 1 , 0 , 1],
[1 , 0 , 0 , 1 , 1 , 1],
[1 , 1 , 0 , 0 , 0 , 1],
[0 , 0 , 1 , 1 , 0 , 1]]

#construction of maze
import networkx as nx
G = nx.Graph()
import matplotlib.pyplot as plt
m=len(maze)
n=len(maze[0])
for i in range(m):
    for j in range(n):
        if maze[i][j]==1:
            G.add_node((i,j))

for i in range(0,m):
    for j in range(0,n-1):
        if maze[i][j]==1:
            if maze[i][j+1]==1:
                G.add_edge((i,j),(i,j+1))
                
for i in range(0,n):
    for j in range(0,m-1):
        if maze[j][i]==1:
            if maze[j+1][i]==1:
                G.add_edge((j,i),(j+1,i))
                
nx.draw(G, with_labels=True)
plt.show()

def find_index(node):
    for index,val in enumerate(list(G.nodes)):
        if node==val:
            return index
visit=[0]*len(list(G.nodes))
ccnum=[0]*len(list(G.nodes))
def explore(i,v,cc):
    visit[i]=1
    ccnum[i]=cc
    for j in list(G.adj[v]):
        index=find_index(j)
        if visit[index]==0:
            print(j)
            explore(index,j,cc)
    
def DFS(nodes):
    cc=0
    for index,val in enumerate(nodes):
        if visit[index]==0:
            explore(index,val,cc)
            cc+=1
DFS(list(G.nodes))

print(ccnum)