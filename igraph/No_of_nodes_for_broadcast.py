from collections import defaultdict
class Number_of_sources:
  
    # to iniialize the class object with the number of vertices asked by the user and also create an adjacency list
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list)
        
    # to add edges provided by the user in the adjacancy list
    def addEdge(self,u,v):
        self.graph[u].append(v)

    """this is inorder to perform DFS on the given graph and push the nodes 
    in the stack according to their post order numbering
    and which will be used later on to convert the provided graph with it's 
    reverse graph"""
    def explore(self,v,visited, stack):
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False:
                self.explore(i, visited, stack)

        stack = stack.append(v)


    """This is method which is used to reverse graph G=(V, E) to G=(V',E'). 
    Such that for every edge (u,v) in E, there will exist an edge(v,u) in 
    E' in G'.
    This way we can have reverse graph and will be used later on to decide the 
    requirements of the class"""
    def reverse_graph(self):
        g = Number_of_sources(self.V)
 

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g