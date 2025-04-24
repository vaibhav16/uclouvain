import unittest

class TestMatToList(unittest.TestCase):
    
    def test_given_example(self):
        adj_mat = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        expected = [[1, 3], [2], [0], [4], [3], []]
        from adj_matrix import mat_to_list 
        self.assertEqual(mat_to_list(adj_mat), expected)

if __name__ == "__main__":
    unittest.main()
