from collections import defaultdict
class Number_of_sources:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list)
        

    def addEdge(self,u,v):
        self.graph[u].append(v)