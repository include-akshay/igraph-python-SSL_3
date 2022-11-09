import igraph as ig
from igraph import *
UG = ig.Graph()
UG.add_vertex('a')
UG.add_vertex('b')
UG.add_vertex('c')
UG.add_vertex('d')
UG.add_edge('a','d')
UG.add_edge('a','c')
UG.add_edge('b','c')
UG.add_edge('b','a')

layout = UG.layout_kamada_kawai()
#UG.write_svg("desk_test")
plot(UG,"nitesh.pdf",layout = layout)
