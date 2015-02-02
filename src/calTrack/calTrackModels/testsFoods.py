from django.utils import unittest
from calTrack.calTrackModels.foods import Foods


class FoodTestCase(unittest.TestCase):
	def setUp(self):
		self.food = Foods(fName = "cheese burger", fCalorie = "20",fType="L")

	def test_Foods (self):
		self.assertEqual(self.food.fName,'cheese burger')