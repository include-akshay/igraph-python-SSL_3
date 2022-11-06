from collections import defaultdict
class Number_of_sources:
  
    # to iniialize the class object with the number of vertices asked by the user and also create an adjacency list
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list)
        
    # to add edges provided by the user in the adjacancy list
    def addEdge(self,u,v):
        self.graph[u].append(v)

    """this is inorder to perform DFS on the given graph and push the nodes in the stack according to their post order numbering
    and which will be used later on to convert the provided graph with it's reverse graph"""
    def explore(self,v,visited, stack):
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False:
                self.explore(i, visited, stack)

        stack = stack.append(v)