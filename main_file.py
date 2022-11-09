import igraph as ig
from igraph import *
g = ig.Number_of_sources(8)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 7)
g.addEdge(3, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(4, 6)

print("")
print("These are the nodes that the network admin should send the message inorder to find the minimum number of nodes"+ 
" to send a message inorder to get it broadcasted : " + str(g.nodes_for_broadcasting()))

# print("Cliques of size three in the provided graph are : "+str(ig.findCliques(0, 1, 3)))

#creating a graph and frquency band method
graph1 = ig.minimum_frequency_bands(10)
graph1.addEdge(0,1)
graph1.addEdge(0,2)
graph1.addEdge(0,3)
graph1.addEdge(0,4)
graph1.addEdge(0,5)
graph1.addEdge(0,6)
graph1.addEdge(0,7)
graph1.addEdge(0,8)
graph1.addEdge(0,9)

print("")
number_of_bands, freq_to_nodes, graph_to_plot=graph1.frequency_band()
print("Least Number of frequencies required are : "+str(number_of_bands))
# layout = graph_to_plot.layout_kamada_kawai()
# color_dict={0: "blue",1:"red",2:"green",3:"yellow", 4:"white", 5:"balck" }
# plot(graph_to_plot,layout = layout,vertex_color =[color_dict[i] for i in freq_to_nodes])



