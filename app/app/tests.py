from django.test import TestCase
from app.calc import add,subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added"""
        self.assertEqual(add(8,9),17)

    def test_subtract_numbers(self):
        """Test that two numbers are added"""
        self.assertEqual(subtract(18,5),13)
