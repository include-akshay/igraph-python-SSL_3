from collections import defaultdict
class Number_of_sources:
  
    """to iniialize the class object with the number of vertices asked by 
    the user and also create an adjacency list"""
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list)
        
    """to add edges provided by the user in the adjacancy list"""
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

    """This is the main method which would be called by the user in order to get 
    results for the query : How many nodes should the network admin send a message 
    in order to get it broadcasted to all the nodes/users/systems in the provided 
    network."""
    def nodes_for_broadcasting(self):
         
        stack = []
        visited =[False]*(self.V)
        for i in range( self.V ):
            if visited[i]==False:
                self.explore( i, visited, stack )
        
        gr = self.reverse_graph()

        visited =[False]*(self.V)
        leader=[]
        for i in range (0, self.V):
            leader.append(i)

        while stack:
           
            i = stack.pop()
            #print(i)
            if visited[i]==False:
                list=gr.SCC_helper(i, visited)
                for j in list:
                    leader[j] =list[0]

        hash=[0]*(self.V)
        for i in range(self.V):
            for j in self.graph[i]:
                if (leader[i]!=leader[j]):
                    for k in range(0, len(leader)):
                        if (leader[k]==leader[j]):
                            hash[k]+=1

        no_incoming_edge=[]
        for i in range(0, len(hash)):
            if(hash[i]==0):
                no_incoming_edge.append(leader[i])  

        no_incoming_edge=set(no_incoming_edge)
        for i in no_incoming_edge:
            print (i)