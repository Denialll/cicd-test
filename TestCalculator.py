import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator()

  def test_add(self):
    self.assertEqual(self.calculator.add(4,7), 11)

if __name__ == "__main__":
  unittest.main()