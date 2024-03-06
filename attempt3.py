import unittest
from remove_transitive_edges import simplify
#from graph import *
from graph_copy import *

graph = Graph({"A":{"B":1, "C":1}, "B":{"C":1}})

#GOOD
def neighbors(x, i):
    j = i
    while j > 0:
        neighbors = graph.edges[x]
        #print(neighbors)
        j =- 1
    return neighbors

neighbors("A", 2)
neighbors("B")
neighbors("C")


for i in range(2, len(graph.nodes())):
    for n1, n2s in graph.edges.items():
        #print(n1)
        #print(n2s)
        for n2 in n2s:
            #print(n2)
            if n2 in n2s:
                print(n2)
        #print(neighbors(n1))



print(graph.edges.items())






#GOOD
for key in (neighbors("A")):
    if key in neighbors("B"):
        print(key, end=" ")





def neighbors(x):
    neighbors = graph.edges[x]
    return neighbors

def next_neighbors(x):
    for n in neighbors:
        next_neighbors = neighbors(n)
        return next_neighbors
        print(next_neighbors)

neighbors("A")
next_neighbors("A")
graph.edges["A"]