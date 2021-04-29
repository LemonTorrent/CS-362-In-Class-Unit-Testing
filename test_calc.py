import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        # passed conditions:
        self.assertEqual(calc.add(2, 1), 3)
        self.assertEqual(calc.sub(4, 2), 2)
        self.assertEqual(calc.mul(3, 9), 27)
        self.assertEqual(calc.div(9, 3), 3)
        self.assertEqual(calc.errorHandle(3, 2), True)

        # failed conditions:
        self.assertEqual(calc.errorHandle(3, "two"), True)
        self.assertEqual(calc.add(2, 9), 7)
        self.assertEqual(calc.sub(0, 4), 1)
        self.assertEqual(calc.mul(3, 9), 27)
        self.assertEqual(calc.div(10, 3), -1)

if __name__ == '__main__':
    unittest.main()
