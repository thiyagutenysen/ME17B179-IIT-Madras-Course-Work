# -*- coding: utf-8 -*-
"""
#BT3051 Assignment 3b
#Roll number: ME17B179
#Time: 1:15
"""

#Header Information

def maze(maze,origin,end):
    #MazeMatrix is a binary matrix (2D list of lists)
    #start & finish are tuples containing the starting and finishing point indices e.g. (1,1) & (5,5)
    
    #import statements, function body
    #construction of maze
    import networkx as nx
    G = nx.Graph()
    import matplotlib.pyplot as plt
    m=len(maze)
    n=len(maze[0])
    
    
    def MazeMatrix2Graph(maze):
        #MazeMatrix is a binary matrix (2D list of lists)
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
                        
        #nx.draw(G, with_labels=True)
        #function body
        
         #a networkx graph whose nodes represent the '1's in the input matrix. node labels are tuples.
    
    def shortest_distance(origin,end):
        
        
        #MazeGraph is a networkx graph 
        #start and finish are tuples containing the starting and finishing point indices
        
        #function body
        pred=[-1]*len(list(G.nodes))
        flag=[False]*len(list(G.nodes))
        q=[]
        index=find_index(origin)
        flag[index]=True
        q.append(origin)
        while(q!=[]):
            v=q.pop(0)
            for w in list(G.adj[v]):
                index=find_index(w)
                if flag[index]==False:
                    flag[index]=True
                    pred[index]=v
                    q.append(w)
    
        shortest_path=[]
        def print_path(pred,end):
            path=[]
            path.append(end)
            index=find_index(end)
            node=pred[index]
            while(node!=origin):
                path.append(node)
                index=find_index(node)
                node=pred[index]
            path.append(origin)
            path.reverse()
            return path
        shortest_path=print_path(pred,end)
        return shortest_path #list of tuples containing indices of the points in the answer
    
    def MazeComponentsDFS():
        #MazeGraph is a networkx graph
        
        #function body  
        
        visit=[0]*len(list(G.nodes))
        ccnum=[0]*len(list(G.nodes))
        def explore(i,v,cc):
            visit[i]=1
            ccnum[i]=cc
            for j in list(G.adj[v]):
                index=find_index(j)
                if visit[index]==0:
                    explore(index,j,cc)
    
        def DFS(nodes):
            cc=0
            for index,val in enumerate(nodes):
                if visit[index]==0:
                    explore(index,val,cc)
                    cc+=1
        DFS(list(G.nodes))
        
        list1=[]
        ccomp=[]
        for i in range(max(ccnum)+1):
            ccomp.append(list1.copy())
        
        def connected_components(ccnum):
            for i,val in enumerate(ccnum):
                ccomp[val].append(list(G.nodes)[i])
            
        connected_components(ccnum)
        return ccomp #list of lists, each containing tuples of the indices of points in that component
    
    #function body
    MazeMatrix2Graph(maze)
    
    def find_index(node):
        for index,val in enumerate(list(G.nodes)):
            if node==val:
                return index
    print('\n')
    print(shortest_distance(origin,end))
    print('\n')
    print(MazeComponentsDFS())
    #a is the output of MazeAnswerBFS and b is the output of MazeComponentsDFS

if __name__ == '__main__':
    #DO NOT MODIFY THE FOLLOWING
    hw3bmaze=    [[1,0,1,1,0,1],
                  [1,1,0,0,0,0],
                  [0,1,0,1,1,1],
                  [0,1,1,1,0,1],
                  [1,0,0,1,1,1],
                  [1,1,0,0,0,1],
                  [0,0,1,1,0,1]]
    
    hw3bstart=(0,0)
    hw3bfinish=(6,5)
    maze(hw3bmaze,hw3bstart,hw3bfinish)
    
#output for this example should be:
#[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5)]
#[[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (3, 5), (2, 5), (2, 4), (2, 3)], [(0, 2), (0, 3)], [(0, 5)], [(4, 0), (5, 0), (5, 1)], [(6, 2), (6, 3)]]