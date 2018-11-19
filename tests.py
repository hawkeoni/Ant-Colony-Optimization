import numpy as np


import unittest
import os

from Generator import CompleteGraph


class TestCompleteGraph(unittest.TestCase):

    def setUp(self):
        self.matrix = np.array([
            [1, 2, 3],
            [0, 4, 5],
            [0, 0, 6]])
        self.filename = "test.xml"

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_init_random(self):
        g = CompleteGraph(nodes=5, low=1, high=2)
        self.assertEqual(g.nodes, 5)
        self.assertEqual(g[1, 0], 1)

    def test_init_matrix(self):
        matrix = np.random.randint(1, 5, (5, 5))
        g = CompleteGraph(matrix=matrix)
        self.assertEqual(g.nodes, 5)
        self.assertEqual(g[3, 2], matrix[3][2])

    def test_randomize(self):
        g = CompleteGraph(nodes=5, low=1, high=2)
        g.randomize(1, 2)
        self.assertEqual(g.nodes, 5)
        self.assertEqual(g[3, 2], 1)

    def test_upper_triangle(self):
        g = CompleteGraph(matrix=self.matrix)
        self.assertEqual(g[0, 2], g[2, 0])

    def test_serialize_deserialize(self):
        g = CompleteGraph(matrix=self.matrix)
        g.to_xml(self.filename)
        b = CompleteGraph(7)
        b.from_xml(self.filename)
        self.assertEquals(b.nodes, 3)
        self.assertTrue((b._matrix == np.array([[0, 2, 3], [0, 0, 5], [0, 0, 0]])).all())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompleteGraph)
    unittest.TextTestRunner(verbosity=2).run(suite)