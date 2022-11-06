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


g.printSCCs()