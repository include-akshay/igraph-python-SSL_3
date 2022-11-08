import sys
import unittest
from collections import defaultdict
sys.path.append('/home/anurag/work/ass3/ass3/igraph-python-SSL_3/igraph')
import No_of_nodes_for_broadcast

graph = No_of_nodes_for_broadcast.Number_of_sources(5)

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
graph.addEdge(3, 4)


class AttributeTest(unittest.TestCase):
    def testreverse_graph(self):
        reverse_list = graph.reverse_graph()
        self.assertDictEqual(reverse_list.__dict__['graph'],{1: [0], 2: [0, 1], 3: [1, 2], 4: [3]},"Unequal dict")


 



