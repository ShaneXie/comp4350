from django.utils import unittest
from calTrack.calTrackModels.foods import Foods


class FoodTestCase(unittest.TestCase):

	def createFood(self, fName = "Test", fCalorie = "20", fType = "L" ):
		return Foods(fName=fName,fCalorie=fCalorie,fType=fType)

	def testFoodsCreation(self):

		food = self.createFood()
		self.assertTrue(isinstance(food, Foods))
		self.assertTrue(food.__unicode__(),food.fName)
		
	

