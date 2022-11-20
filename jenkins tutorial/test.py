import unittest

from add import add

class TestSum(unittest.TestCase):
    def test_int(self):

        a = 1
        b = 2
        result = add(a,b)
        self.assertEqual(result, 3)
        
    def test_str(self):

        a = "Shreyash"
        b = "Deshpande"
        result = add(a,b)
        self.assertEqual(result, "ShreyashDeshpande")
        
    def test_list(self):

        a = [1,2,3]
        b = [3,4,5]
        result = add(a,b)
        self.assertEqual(result, [1,2,3,3,4,5])

if __name__ == '__main__':
    unittest.main()
