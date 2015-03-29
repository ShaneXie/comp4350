from django.utils import unittest
from calTrack.models import Foods
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class FoodTestCase(unittest.TestCase):

	def setUp(self):
		pass

	def testFoodsCreation(self):

		food = Foods(fName = "Test", fCalorie = "20", fType = "Lunch" )
		self.assertTrue(isinstance(food, Foods))
		self.assertEqual(food.__unicode__(),food.fName)

	def testValidationsInvalidCalories(self):

		zeroFoodCalories = Foods(fName = "Zero Calories", fCalorie = "0", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if zeroFoodCalories.full_clean():
				zeroFoodCalories.save()

		self.assertEqual(Foods.objects.filter(fName="Zero Calories").count(), 0)
		

		negativeFoodCalories = Foods(fName = "Negative Calories", fCalorie = "-1", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if negativeFoodCalories.full_clean():
				negativeFoodCalories.save()

		self.assertEqual(Foods.objects.filter(fName="Negative Calories").count(), 0)

		nullFoodCalories = Foods(fName = "Null Calories", fCalorie = "", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if nullFoodCalories.full_clean():
				nullFoodCalories.save()

		self.assertEqual(Foods.objects.filter(fName="Null Calories").count(), 0)


	
	def testValidationsvalidCalories(self):

		validFoodCalories = Foods(fName = "Valid Calories", fCalorie = "100", fType = "Lunch" )

		self.assertRaises(ValidationError,validFoodCalories.full_clean())
		validFoodCalories.save()

		self.assertNotEqual(Foods.objects.filter(fName="Valid Calories").count(), 0)
		self.assertEqual(Foods.objects.filter(fName="Valid Calories").count(), 1)


	def testValidationInvalidFoodTypes(self):

		foodTypeInvalid = Foods(fName = "z is not a valid food type", fCalorie = "100", fType = "Zin" )

		with self.assertRaises(ValidationError):
			if foodTypeInvalid.full_clean():
				foodTypeInvalid.save()


		foodTypeInvalidCapital = Foods(fName = "A is not a valid food type", fCalorie = "100", fType = "LUNCH" )
		
		with self.assertRaises(ValidationError):
			if foodTypeInvalidCapital.full_clean():
				foodTypeInvalidCapital.save()

		self.assertEqual(Foods.objects.filter(fName="A is not a valid food type").count(), 0)


		foodTypeInvalidDueToSmall = Foods(fName = "Capital B is not a valid food type", fCalorie = "100", fType = "breakfast" )
		
		with self.assertRaises(ValidationError):
			if foodTypeInvalidDueToSmall.full_clean():
				foodTypeInvalidDueToSmall.save()

		self.assertEqual(Foods.objects.filter(fName="Capital B is not a valid food type").count(), 0)


	def testValidationvalidFoodTypes(self):

		validFoodTypeBreakfast = Foods(fName = "BreakFast", fCalorie = "100", fType = "Breakfast" )

		self.assertRaises(ValidationError,validFoodTypeBreakfast.full_clean())
		validFoodTypeBreakfast.save()

		self.assertNotEqual(Foods.objects.filter(fName="BreakFast").count(), 0)
		self.assertEqual(Foods.objects.filter(fName="BreakFast").count(), 1)


		validFoodTypeLunch = Foods(fName = "Lunch", fCalorie = "100", fType = "Lunch" )

		self.assertRaises(ValidationError,validFoodTypeLunch.full_clean())
		validFoodTypeLunch.save()

		self.assertNotEqual(Foods.objects.filter(fName="Lunch").count(), 0)
		self.assertEqual(Foods.objects.filter(fName="Lunch").count(), 1)

		validFoodTypeDinner = Foods(fName = "Dinner", fCalorie = "100", fType = "Dinner" )

		self.assertRaises(ValidationError,validFoodTypeDinner.full_clean())
		validFoodTypeDinner.save()

		self.assertNotEqual(Foods.objects.filter(fName="Dinner").count(), 0)
		self.assertEqual(Foods.objects.filter(fName="Dinner").count(), 1)

		validFoodTypeSnacks = Foods(fName = "Snacks", fCalorie = "100", fType = "Snacks" )

		self.assertRaises(ValidationError,validFoodTypeSnacks.full_clean())
		validFoodTypeSnacks.save()

		self.assertNotEqual(Foods.objects.filter(fName="Snacks").count(), 0)
		self.assertEqual(Foods.objects.filter(fName="Snacks").count(), 1)


	def testValidationInvalidFoodNames(self):

		FoodNameWithNumberAtStartIsInvalid = Foods(fName = "1one", fCalorie = "100", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if FoodNameWithNumberAtStartIsInvalid.full_clean():
				FoodNameWithNumberAtStartIsInvalid.save()

		self.assertEqual(Foods.objects.filter(fName="1one").count(), 0)


		FoodNameWithNumberAtEndIsInvalid = Foods(fName = "two2", fCalorie = "100", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if FoodNameWithNumberAtEndIsInvalid.full_clean():
				FoodNameWithNumberAtEndIsInvalid.save()

		self.assertEqual(Foods.objects.filter(fName="two2").count(), 0)

		FoodNameWithNumberAtMiddleIsInvalid = Foods(fName = "two2two", fCalorie = "100", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if FoodNameWithNumberAtMiddleIsInvalid.full_clean():
				FoodNameWithNumberAtMiddleIsInvalid.save()

		self.assertEqual(Foods.objects.filter(fName="two2two").count(), 0)

		FoodNameWithOnlyNumbersIsInvalid = Foods(fName = "123456", fCalorie = "100", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if FoodNameWithOnlyNumbersIsInvalid.full_clean():
				FoodNameWithOnlyNumbersIsInvalid.save()

		self.assertEqual(Foods.objects.filter(fName="two2two").count(), 0)

	def testValidationValidFoodNames(self):

		validFoodNameCheeseBurger = Foods(fName = "Cheese Burger", fCalorie = "100", fType = "Lunch" )

		self.assertRaises(ValidationError,validFoodNameCheeseBurger.full_clean())
		validFoodNameCheeseBurger.save()
		self.assertEqual(Foods.objects.filter(fName="Cheese Burger").count(), 1)


		validFoodNameChickenBurger = Foods(fName = "Chicken Burger", fCalorie = "100", fType = "Lunch" )

		self.assertRaises(ValidationError,validFoodNameChickenBurger.full_clean())
		validFoodNameChickenBurger.save()
		self.assertEqual(Foods.objects.filter(fName="Chicken Burger").count(), 1)

	def testValidationFoodNamesForDuplicates(self):

		self.assertEqual(Foods.objects.filter(fName="Original").count(), 0)

		originalFoodName = Foods(fName = "Original", fCalorie = "100", fType = "Lunch" )

		originalFoodName.save()

		self.assertEqual(Foods.objects.filter(fName="Original").count(), 1)

		duplicateFoodName = Foods(fName = "Original", fCalorie = "100", fType = "Lunch" )

		with self.assertRaises(ValidationError):
			if duplicateFoodName.full_clean():
				duplicateFoodName.save()

		self.assertNotEqual(Foods.objects.filter(fName="Original").count(), 2)
		self.assertEqual(Foods.objects.filter(fName="Original").count(), 1)

	def tearDown(self):
		Foods.objects.all().delete()





