from django.test import TestCase
from calTrack.models import Foods, UserProfile

class ViewTestCase(TestCase):
	fixtures = ['calTrackViewsTestdata.json']

	def testInvalidIndexView(self):
		response = self.client.get('/index/')
		self.assertEqual(response.status_code,404)


	def testIndexView(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'index.html')
		self.assertTrue('csrf_token' in response.context)
		self.assertTrue('user' in response.context)

	def testinvalidAjax(self):
		response = self.client.get('/ajax/')
		self.assertEqual(response.status_code,404)

	def testAjaxGetAllFood(self):
		response = self.client.get('/ajax/getAllFood/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'foodlist.html')
		self.assertTrue('csrf_token' in response.context)
		self.assertTrue('foodList' in response.context)
		self.assertNotEqual(response.context['foodList'].count(),0)
		self.assertEqual(response.context['foodList'].count(),8)
		self.assertEqual([tracker.pk for tracker in response.context['foodList']], [1,2,3,4,5,6,7,8])
		foodInstance = response.context['foodList'][0]
		self.assertEqual(foodInstance.pk,1)
		self.assertEqual(foodInstance.fType,"d")
		self.assertEqual(foodInstance.fCalorie,100)
		self.assertEqual(foodInstance.fName,"Chicken Burger")

	def testAjaxGetLoginItem(self):
		response = self.client.get('/ajax/getLoginItem/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'loginNavItem.html')
		self.assertTrue('csrf_token' in response.context)
		self.assertTrue('user' in response.context)
		self.assertTrue(response.context['user'].is_anonymous())

	def testAjaxLogin(self):





