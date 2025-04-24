import unittest

class TestReachableFunction(unittest.TestCase):
    def test_from_node_0(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        from reachable_nodes import reachable
        result = reachable(adj_list, 0)
        expected = {0, 1, 2, 3, 4}
        self.assertEqual(result, expected)

    def test_from_node_3(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        from reachable_nodes import reachable
        result = reachable(adj_list, 3)
        expected = {3, 4}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
