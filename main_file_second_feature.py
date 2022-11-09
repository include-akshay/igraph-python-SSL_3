import igraph as ig
from igraph import *

# print("Cliques of size three in the provided graph are : "+str(ig.findCliques(0, 1, 3)))

#creating a graph and frquency band method
graph4 = ig.minimum_frequency_bands(4)

graph4.addEdge(0,1)
graph4.addEdge(0,2)
graph4.addEdge(1,2)
graph4.addEdge(1,3)
graph4.addEdge(2,3)
graph4.addEdge(3,0)

print("")
number_of_bands, freq_to_nodes, graph_to_plot=graph4.frequency_band()
print("Least Number of frequencies required are : "+str(number_of_bands))
# layout = graph_to_plot.layout_kamada_kawai()
# color_dict={0: "blue",1:"red",2:"green",3:"yellow", 4:"white", 5:"balck" }
# plot(graph_to_plot,layout = layout,vertex_color =[color_dict[i] for i in freq_to_nodes])







