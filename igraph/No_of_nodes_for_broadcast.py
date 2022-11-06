from collections import defaultdict

__all__ =("Number_of_sources",
"addEdge",
"explore",
"reverse_graph",
"SCC_helper",
"nodes_for_broadcasting",
)

class Number_of_sources:
    """It finds the names of the nodes,the network admin should send a message 
    in order to get it broadcasted to all the nodes/users/systems in the provided 
    network.
    This is to help a network admin by getting his/her work get minimized by providing
    them the least number of node names to send a message"""
  
    
    def __init__(self,vertices):
        """to iniialize the class object with the number of vertices asked by 
        the user and also create an adjacency list.
        @param vertices : It is the number of vertices in the graph that 
        is to be analysed and it is supposed to be provided by the user when creating
        a object of the class. """
        self.V= vertices 
        self.graph = defaultdict(list)
        
    
    def addEdge(self,u,v):
        """to add edges provided by the user in the adjacancy list.
        @param u : The souce node.
        
        @param v : The destination node."""
        self.graph[u].append(v)

    
    def explore(self,v,visited, stack):
        """this is inorder to perform DFS on the given graph and push the nodes 
        in the stack according to their post order numbering.
        And which will be used later on to convert the provided graph with it's 
        reverse graph.
        @param v: the node whose expolration is supposed to be done

        @param visited : the array to keep check if a certain has been visited already
                in order to avoid into getting infinite loops

        @ param stack : a stack for us to keep track of the nodes according to their
                post numbers"""
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False:
                self.explore(i, visited, stack)

        stack = stack.append(v)


    
    def reverse_graph(self):
        """This is method which is used to reverse graph G=(V, E) to G=(V',E'). 
        Such that for every edge (u,v) in E, there will exist an edge(v,u) in 
        E' in G'.
        This way we can have reverse graph which will be used later on to decide the 
        requirements of the class
        @param : self, it is the object that called this function
        @return : reversed Graph G' """
        g = Number_of_sources(self.V)
 

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    
    def SCC_helper(self,v,visited):
        """This method tells the main function which are the Strongly connected components
        So that it can get hand on the nodes to which the admin should send the msg inorder
        to get it broadcasted
        
        @param v : node through which we will do the exploration on the reversed graph
        
        @param visited :the array to keep check if a certain has been visited already
                         in order to avoid into getting infinite loops.
        
        @return : A list which contains all the nodes of a specific Strongly Connected 
                  component."""
        visited[v]= True
        main_list=[]
        for i in self.graph[v]:
            if visited[i]==False:
                list=self.DFSUtil(i,visited)
                for j in list:
                    main_list.append(j)
        main_list.append(v)
        return main_list

    
    def nodes_for_broadcasting(self):
        """This is the main method which would be called by the user in order to get 
        results for the query : How many nodes should the network admin send a message 
        in order to get it broadcasted to all the nodes/users/systems in the provided 
        network.
        
        @returns : prints the names of the nodes to whom the network admin should send
        the message inorder to get the message broadcasted"""
         
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