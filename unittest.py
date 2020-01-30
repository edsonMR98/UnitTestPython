from funcs import *
import unittest

class operationsTest(unittest.TestCase):
    def setUp(self):
        # Here executes what it should be executed before a test starts
        pass

    def testSuma(self):
        waited = 3
        current = suma(2, 1)
        self.assertEqual(current, waited)

    def testResta(self):
        waited = 3
        current = resta(6, 3)
        self.assertEqual(current, waited)

    def testMultiplicacion(self):
        waited = 10
        current = multiplicacion(5, 2)
        self.assertEqual(current, waited)

    def testDivision(self):
        waited = 5
        current = division(10, 2)
        self.assertEqual(current, waited)

    def tearDown(self):
        # Here executes waht ii should be executed after a test
        pass

if __name__ == '__main__':
    unittest.main()