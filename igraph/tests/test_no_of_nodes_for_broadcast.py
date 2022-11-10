import sys
import unittest
from collections import defaultdict
sys.path.append('/home/anurag/work/IITD/COP701/igraph-python-SSL_3/igraph')
import No_of_nodes_for_broadcast

graph = No_of_nodes_for_broadcast.Number_of_sources(5)

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
graph.addEdge(3, 4)




g1 = No_of_nodes_for_broadcast.Number_of_sources(8)
g1.addEdge(0, 3)
g1.addEdge(0, 4)
g1.addEdge(1, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 7)
g1.addEdge(3, 5)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)

g2=No_of_nodes_for_broadcast.Number_of_sources(4)
g2.addEdge(1,0)
g2.addEdge(1,2)
g2.addEdge(2,0)
g2.addEdge(2,3)
g2.addEdge(3,2)


g3 =No_of_nodes_for_broadcast.Number_of_sources(6)
g3.addEdge(0,1)
g3.addEdge(1,2)
g3.addEdge(2,4)
g3.addEdge(4,3)
g3.addEdge(3,1)
g3.addEdge(4,5)

g4=No_of_nodes_for_broadcast.Number_of_sources(5)
g4.addEdge(0,3)
g4.addEdge(0,2)
g4.addEdge(1,0)
g4.addEdge(2,1)
g4.addEdge(3,4)
g4.addEdge(4,0)


class AttributeTest(unittest.TestCase):
    def testreverse_graph(self):
        reverse_list = graph.reverse_graph()
        self.assertDictEqual(reverse_list.__dict__['graph'],{1: [0], 2: [0, 1], 3: [1, 2], 4: [3]},"Unequal dict")


    def test_numberofsources1(self):
        answer = g1.nodes_for_broadcasting()
        result = {0, 1, 2}
        self.assertEqual(answer,result,"Unequal")

    def test_numberofsources2(self):
        answer = g2.nodes_for_broadcasting()
        result = {1}
        self.assertEqual(answer,result,"Unequal")

    def test_numberofsources3(self):
        answer = g3.nodes_for_broadcasting()
        result = {0}
        self.assertEqual(answer,result,"Unequal")

    def test_numberofsources4(self):
        answer = g4.nodes_for_broadcasting()
        result = {2}
        self.assertEqual(answer,result,"Unequal")







