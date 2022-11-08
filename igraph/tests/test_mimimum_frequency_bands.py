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

graph1 = minimum_frequency_bands.minimum_frequency_bands(10)
graph1.addEdge(0,1)
graph1.addEdge(0,2)
graph1.addEdge(0,3)
graph1.addEdge(0,4)
graph1.addEdge(0,5)
graph1.addEdge(0,6)
graph1.addEdge(0,7)
graph1.addEdge(0,8)
graph1.addEdge(0,9)


graph2 = minimum_frequency_bands.minimum_frequency_bands(4)
graph2.addEdge(0,1)
graph2.addEdge(1,2)
graph2.addEdge(2,3)
graph2.addEdge(3,0)

#test3 odd length simple cycle
graph3 = minimum_frequency_bands.minimum_frequency_bands(5)
graph3.addEdge(0,1)
graph3.addEdge(1,2)
graph3.addEdge(2,3)
graph3.addEdge(3,4)
graph3.addEdge(4,0)
#expected output = 3
#[0,1,0,1,2]

#test4 complete graph
graph4 = minimum_frequency_bands.minimum_frequency_bands(4)
graph4.addEdge(0,1)
graph4.addEdge(0,2)
graph4.addEdge(1,2)
graph4.addEdge(1,3)
graph4.addEdge(2,3)
graph3.addEdge(3,0)
#expected output = 4


#test5 line graph
graph5 = minimum_frequency_bands.minimum_frequency_bands(6)
graph5.addEdge(0,1)
graph5.addEdge(1,2)
graph5.addEdge(2,3)
graph5.addEdge(3,4)
graph5.addEdge(4,5)
#expected output = 2

class AttributeTest(unittest.TestCase):
    def testaddEdge(self):
        value_len , result = graph.frequency_band()
        self.assertEqual(value_len,3,"Value len unequal")

    def testaddEdge_list(self):
        value_len , result = graph.frequency_band()
        self.assertListEqual(result,[0, 1, 2, 0, 1],"List not equal")

    def testaddEdge1(self):
        value_len1 , result1 = graph1.frequency_band()
        self.assertEqual(value_len1,2,"Value len unequal")

    def testaddEdge_list1(self):
        value_len1 , result1 = graph1.frequency_band()
        self.assertListEqual(result1,[0,1,1,1,1,1,1,1,1,1],"List not equal")

    def testaddEdge2(self):
        value_len2 , result2 = graph2.frequency_band()
        self.assertEqual(value_len2,2,"Value len unequal")

    def testaddEdge_list2(self):
        value_len2 , result2 = graph2.frequency_band()
        self.assertListEqual(result2,[0,1,0,1],"List not equal")

#Test4 odd length simple cycle

    def testaddEdge3(self):
        value_len3 , result3 = graph3.frequency_band()
        self.assertEqual(value_len3,3,"Value len unequal")

    def testaddEdge_list3(self):
        value_len3 , result3 = graph3.frequency_band()
        self.assertListEqual(result3,[0,1,0,1,2],"List not equal")


    def testaddEdge4(self):
        value_len4 , result4 = graph4.frequency_band()
        self.assertEqual(value_len4,3,"Value len unequal")

    def testaddEdge_list4(self):
        value_len4 , result4 = graph4.frequency_band()
        self.assertListEqual(result4,[0,1,2,0],"List not equal")


    def testaddEdge5(self):
        value_len5 , result5 = graph5.frequency_band()
        self.assertEqual(value_len5,2,"Value len unequal")

    def testaddEdge_list5(self):
        value_len5 , result5 = graph5.frequency_band()
        self.assertListEqual(result5,[0,1,0,1,0,1],"List not equal")

   

    

    



