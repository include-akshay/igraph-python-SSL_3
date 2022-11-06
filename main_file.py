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


print(f"These are the nodes that the network admin should send the message inorder to find the minimum number of nodes to send a message inorder to get it broadcasted :  " + str(g.nodes_for_broadcasting()))
print("")
# print("Cliques of size three in the provided graph are : "+str(ig.findCliques(0, 1, 3)))

