import unittest
import sys
from collections import defaultdict
sys.path.append('/home/anurag/work/ass3/ass3/igraph-python-SSL_3/igraph')
import minimum_frequency_bands
graph = minimum_frequency_bands.minimum_frequency_bands(5)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
graph.addEdge(3, 4)

class AttributeTest(unittest.TestCase):
    def testaddEdge(self):
        value_len , result = graph.frequency_band()
        self.assertEqual(value_len,3,"Value len unequal")

    def testaddEdge_list(self):
        value_len , result = graph.frequency_band()
        self.assertListEqual(result,[0, 1, 2, 0, 1],"List not equal")



