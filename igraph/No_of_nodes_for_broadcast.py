from collections import defaultdict
class Number_of_sources:
  
    # to iniialize the class object with the number of vertices asked by the user and also create an adjacency list
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list)
        
    # to add edges provided by the user in the adjacancy list
    def addEdge(self,u,v):
        self.graph[u].append(v)