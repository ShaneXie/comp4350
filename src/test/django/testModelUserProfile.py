from django.utils import unittest
from calTrack.models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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





