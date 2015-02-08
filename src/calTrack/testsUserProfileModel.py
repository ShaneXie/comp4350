from django.utils import unittest
from calTrack.models import UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserProfileTestCase(unittest.TestCase):

	def testUserProfileCreation(self):

		userProfileTest = UserProfile(user = User(username="Profile Test", password = "hello", first_name = "Fname", last_name = "Lname", email = "ProfileTest@test.com"), age = "20", weight = "60", height = "124", gender = "m" )
		self.assertTrue(isinstance(userProfileTest, UserProfile))
		self.assertEqual(userProfileTest.__unicode__(),' '.join([
            userProfileTest.user.first_name,
            userProfileTest.user.last_name,
        ]))
