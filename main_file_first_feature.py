import igraph as ig
from igraph import *

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

# g=ig.Number_of_sources(4)
# g.addEdge(1,0)
# g.addEdge(1,2)
# g.addEdge(2,0)
# g.addEdge(2,3)
# g.addEdge(3,2)

# g =ig.Number_of_sources(6)
# g.addEdge(0,1)
# g.addEdge(1,2)
# g.addEdge(2,4)
# g.addEdge(4,3)
# g.addEdge(3,1)
# g.addEdge(4,5)

# g=ig.Number_of_sources(5)
# g.addEdge(0,3)
# g.addEdge(0,2)
# g.addEdge(1,0)
# g.addEdge(2,1)
# g.addEdge(3,4)
# g.addEdge(4,0)
print("")
print("These are the nodes that the network admin should send the message inorder to find the minimum number of nodes"+ 
" to send a message inorder to get it broadcasted : " + str(g.nodes_for_broadcasting()))








