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

   



