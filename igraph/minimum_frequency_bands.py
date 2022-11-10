# algorithm for graph coloring
from collections import defaultdict
import igraph as ig 
import datetime

__all__ =(
"addEdge",
"frequency_band",
)
class minimum_frequency_bands:
   
    def __init__(self,vertices):
        """to iniialize the class object with the number of vertices asked by 
        the user and also create an adjacency list.
        
        @param vertices : It is the number of vertices in the graph that 
        is to be analysed and it is supposed to be provided by the user when creating
        a object of the class. """
        self.V= vertices 
        self.adj = defaultdict(list)
        self.graph_to_plot=ig.Graph()
        for i in range(0, self.V):
            self.graph_to_plot.add_vertex(chr(ord('a')+i))

    def addEdge(self, v, w):
         """to add the edges provided by the user in the adjacency list.
         as here the graph is undirected, so it will be added for both the vertex.

         @param u : The source node in edge(u,v) and destination node in edge(v,u)
         @param v : The destination node in edge(u,v) and source node in edge(v,u)
         """
         self.adj[v].append(w)
         self.adj[w].append(v)
         self.graph_to_plot.add_edge(chr(ord('a')+v),chr(ord('a')+w))
            

# Assigns colors (starting from 0) to all
# vertices and prints the assignment of colors
    def frequency_band(self):
        """This method used to find the upper bound of chromatic number.
        The Chromatic number can be used to find the minimum number of different frequency is needed
        to be assigned to a Network,i.e. frequency to be assigned to the same location must be different,
        otherwise they may overlap.
        
        @param result : array used to keep track which tower is given which frequency, initalize with -1 initially.
        
        @param available :  temporary array to store the available colors.
                            True value of available[cr] would mean that the
                            color cr is assigned to one of its adjacent vertices.
                            initially initialize with False.
        
        @return : It returns the number of bands required, a graph object which will help in saving the file.
                  and finally a list which tells the color of the node.
        """
        
        result = [-1] * self.V
        result[0] = 0; # starting with minimum vertex and labelling with minimum color
        available = [False] * self.V

        for u in range(1, self.V):
            
            # Process all adjacent vertices and
            # flag their colors as unavailable
            for i in self.adj[u]:
                if (result[i] != -1):
                    available[result[i]] = True

            # Find the lowest_indexed colors that can be assigned
            color = 0
            while color < self.V:
                if (available[color] == False):
                    break
                
                color += 1
                
            # Assign the found color
            result[u] = color

            # Reset the values back to false
            # for the next iteration
            for i in self.adj[u]:
                if (result[i] != -1):
                    available[result[i]] = False

        layout = self.graph_to_plot.layout_kamada_kawai()
        color_dict={0: "blue",1:"red",2:"green",3:"yellow", 4:"white", 5:"balck" }  
        
        yes_or_no=input("Do you want to save the graph as well :: (y/n)")
        if yes_or_no == 'y' or yes_or_no=='Y':
            name_of_svg=str(datetime.datetime.now())
            name_of_svg=name_of_svg.replace(" ", "")
            name_of_svg=name_of_svg.replace("-", "")
            name_of_svg=name_of_svg.replace(".", "")
            name_of_svg=name_of_svg.replace(":", "")
            

            self.graph_to_plot.write_svg(f"file{name_of_svg}.svg", layout=layout, colors =[color_dict[i] for i in result])

        return(len(set(result)), result, self.graph_to_plot)