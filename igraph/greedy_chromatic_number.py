# algorithm for graph coloring
from collections import defaultdict

__all__ =(
"addEdge",
"greedyColoring"
,
)
class chromatic_number_greedy:
   
    def __init__(self,vertices):
        """to iniialize the class object with the number of vertices asked by 
        the user and also create an adjacency list.
        @param vertices : It is the number of vertices in the graph that 
        is to be analysed and it is supposed to be provided by the user when creating
        a object of the class. """
        self.V= vertices 
        self.adj = defaultdict(list)

    def addEdge(self, v, w):
	
            self.adj[v].append(w)
            self.adj[w].append(v)
            

# Assigns colors (starting from 0) to all
# vertices and prints the assignment of colors
    def greedyColoring(self):
        
        result = [-1] * self.V

       
        result[0] = 0


        
        available = [False] * self.V

        for u in range(1, self.V):
            for i in self.adj[u]:
                if (result[i] != -1):
                    available[result[i]] = True
            color = 0
            while color < self.V:
                if (available[color] == False):
                    break
                
                color += 1
                
            # Assign the found color
            result[u] = color
            for i in self.adj[u]:
                if (result[i] != -1):
                    available[result[i]] = False

        # Print the result
        return (result)

   



