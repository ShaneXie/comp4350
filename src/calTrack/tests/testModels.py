from django.utils import unittest
from calTrack.models import Foods, UserProfile
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

class UserProfileTestCase(unittest.TestCase):
    
	def setUp(self):
		self.userTest = User.objects.create( username="Profile_test", password = "hello", first_name = "Fname", last_name = "Lname", email = "ProfileTest@test.com")
		self.userTest1 = User.objects.create(username="Age_valid_test1", password = "hello", first_name = "Fname", last_name = "Lname", email = "ProfileTest@test.com")

	def testUserProfileCreation(self):

		userProfileTest = UserProfile(user = self.userTest, age = "20", weight = "60", height = "124", gender = "Male" )
		self.assertTrue(isinstance(userProfileTest, UserProfile))
		self.assertEqual(userProfileTest.__unicode__(),' '.join([
            userProfileTest.user.first_name,
            userProfileTest.user.last_name]))

	def testValidationInvalidAge(self):

		userProfileAgeZero = UserProfile(user = self.userTest, age = "0", weight = "60", height = "124", gender = "Female" )
		
		with self.assertRaises(ValidationError):
			if userProfileAgeZero.full_clean():
				userProfileAgeZero.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

		userProfileAgeGreaterThanLimit = UserProfile(user = self.userTest, age = "101", weight = "60", height = "124", gender = "Female" )
		
		with self.assertRaises(ValidationError):
			if userProfileAgeGreaterThanLimit.full_clean():
				userProfileAgeGreaterThanLimit.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

		userProfileAgeLessThanLimit = UserProfile(user = self.userTest, age = "9", weight = "60", height = "124", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileAgeLessThanLimit.full_clean():
				userProfileAgeLessThanLimit.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

	def testValidationsvalidAge(self):

		userProfileValidAge = UserProfile(user = self.userTest, age = "25", weight = "60", height = "124", gender = "Male" )
		
		self.assertRaises(ValidationError,userProfileValidAge.full_clean())
		userProfileValidAge.save()

		self.assertNotEqual(UserProfile.objects.all().count(), 0)
		self.assertEqual(UserProfile.objects.all().count(), 1)


		userProfileValidAge1 = UserProfile(user = self.userTest1, age = "50", weight = "60", height = "124", gender = "Male" )

		self.assertRaises(ValidationError,userProfileValidAge1.full_clean())
		userProfileValidAge1.save()

		self.assertNotEqual(UserProfile.objects.all().count(), 1)
		self.assertEqual(UserProfile.objects.all().count(), 2)

	def testValidationInvalidWeight(self):

		userProfileNegativeWeight = UserProfile(user = self.userTest, age = "20", weight = "-100", height = "124", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileNegativeWeight.full_clean():
				userProfileNegativeWeight.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

		userProfileZeroWeight = UserProfile(user = self.userTest, age = "20", weight = "0", height = "124", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileZeroWeight.full_clean():
				userProfileZeroWeight.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)
		
		userProfileWeightGreaterThanLimit = UserProfile(user = self.userTest, age = "20", weight = "701", height = "124", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileWeightGreaterThanLimit.full_clean():
				userProfileWeightGreaterThanLimit.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

		userProfileWeightLessThanLimit = UserProfile(user = self.userTest, age = "20", weight = "9", height = "124", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileWeightLessThanLimit.full_clean():
				userProfileWeightLessThanLimit.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

	def testValidationValidWeigth(self):


		userProfileValidWeight = UserProfile(user = self.userTest, age = "25", weight = "200", height = "124", gender = "Male" )
		
		self.assertRaises(ValidationError,userProfileValidWeight.full_clean())
		userProfileValidWeight.save()

		self.assertNotEqual(UserProfile.objects.all().count(), 0)
		self.assertEqual(UserProfile.objects.all().count(), 1)
		
		userProfileValidWeight1 = UserProfile(user = self.userTest1, age = "25", weight = "100.5", height = "124", gender = "Male" )
		self.assertRaises(ValidationError,userProfileValidWeight1.full_clean())
		userProfileValidWeight1.save()

		self.assertNotEqual(UserProfile.objects.all().count(), 1)
		self.assertEqual(UserProfile.objects.all().count(), 2)

	def testValidationInvalidHeight(self):
		
		userProfileNegativeHeight = UserProfile(user = self.userTest, age = "20", weight = "150", height = "-1", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileNegativeHeight.full_clean():
				userProfileNegativeHeight.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

		userProfileHeightZero = UserProfile(user = self.userTest, age = "20", weight = "150", height = "0", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileHeightZero.full_clean():
				userProfileHeightZero.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

		userProfileHeightGreaterThanLimit = UserProfile(user = self.userTest, age = "20", weight = "150", height = "251", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileHeightGreaterThanLimit.full_clean():
				userProfileHeightGreaterThanLimit.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

		userProfileHeightLessThanLimit = UserProfile(user = self.userTest, age = "20", weight = "150", height = "49", gender = "Male" )
		
		with self.assertRaises(ValidationError):
			if userProfileHeightLessThanLimit.full_clean():
				userProfileHeightLessThanLimit.save()

		self.assertEqual(UserProfile.objects.all().count(), 0)

	def testValidationValidHeight(self):

		userProfileValidHeight = UserProfile(user = self.userTest, age = "25", weight = "200", height = "150", gender = "Male" )
		
		self.assertRaises(ValidationError,userProfileValidHeight.full_clean())
		userProfileValidHeight.save()

		self.assertNotEqual(UserProfile.objects.all().count(), 0)
		self.assertEqual(UserProfile.objects.all().count(), 1)
		
		userProfileValidWeight1 = UserProfile(user = self.userTest1, age = "25", weight = "200", height = "190.5", gender = "Male" )
		self.assertRaises(ValidationError,userProfileValidWeight1.full_clean())
		userProfileValidWeight1.save()

		self.assertNotEqual(UserProfile.objects.all().count(), 1)
		self.assertEqual(UserProfile.objects.all().count(), 2)


	def tearDown(self):
		User.objects.all().delete()
		UserProfile.objects.all().delete()





