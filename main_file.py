import igraph as ig


g = ig.Number_of_sources(8)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 7)
g.addEdge(3, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(4, 6)

print("")
print("These are the nodes that the network admin should send the message inorder to find the minimum number of nodes to send a message inorder to get it broadcasted :  " )
print("")
source_list=g.nodes_for_broadcasting()
print(source_list)
# print("Cliques of size three in the provided graph are : "+str(ig.findCliques(0, 1, 3)))

#creating a graph and calling coloring method
c = ig.chromatic_number_greedy(5)
c.addEdge(0, 1)
c.addEdge(0, 2)
c.addEdge(1, 2)
c.addEdge(1, 3)
c.addEdge(2, 3)
c.addEdge(3, 4)
print("")
print("Coloring of graph 1 ")
print("")
list_2nd=c.greedyColoring()
print(list_2nd)


