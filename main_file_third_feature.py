from igraph import k_dense_network

obj=k_dense_network.Classname(5)
obj.addEdge(1,2)
obj.addEdge(2,3)
obj.addEdge(3,1)
obj.addEdge(4,3)
obj.addEdge(4,5)
obj.addEdge(5,3)
count_of_cliques,final_result=obj.calling_function(0,1,3)
print("Number of such dense networks :: ", count_of_cliques)
print(final_result)
