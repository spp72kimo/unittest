import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_plus(self):
        expected = 5;
        result = calculator.plus(*self.args);
        self.assertEqual(expected, result);

    def test_minus(self):
        expected = 1;
        result = calculator.minus(*self.args);
        self.assertEqual(expected, result);


# tests = ['test_plus', 'test_minus']
# suite = unittest.TestSuite(map(CalculatorTestCase, tests))

suite = (unittest.TestLoader()
                 .loadTestsFromTestCase(CalculatorTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)