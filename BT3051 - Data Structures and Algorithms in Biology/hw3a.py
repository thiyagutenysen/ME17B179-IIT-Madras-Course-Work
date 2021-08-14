# -*- coding: utf-8 -*-
"""

#BT3051 Assignment 3a
#Roll number: ME17B179
#Time: 1:15

"""

def RegularLattice(nodes, k):
    import networkx as nx
    import matplotlib.pyplot as plt 
    G = nx.Graph()
    for i in range(nodes):
        G.add_node(i)
    for i in range(nodes):
        for j in range(1,k+1):
            if i+j<nodes:
                G.add_edge(i,i+j)
            else:
                G.add_edge(i,i+j-nodes)
            
    nx.draw(G, with_labels=True)
    plt.figure(1,figsize=(12,12)) 
    plt.show()

if _name_ == '_main_':
    RegularLattice(8,3)
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)