from django.test import SimpleTestCase
from utils.numerics import inch_to_centimeter, ounce_to_gram
from random import randint

class TestNumerics(SimpleTestCase): # Must start with "Test"

    def test_inch_to_centimeter(self): # Must start with "test"

        result = inch_to_centimeter(1)
        self.assertEqual(result, 2.54)

        result = inch_to_centimeter(0)
        self.assertEqual(result, 0)

        result = inch_to_centimeter(randint(0, 1000))
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 2540)

        result = inch_to_centimeter(-5)
        self.assertEqual(result, -12.7)
    
    def test_ounce_to_gram(self):
        result = ounce_to_gram(1)
        self.assertEqual(result, 28.35)

        result = ounce_to_gram(0)
        self.assertEqual(result, 0)

        result = ounce_to_gram(-5)
        self.assertEqual(result, -141.75)