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

	def testAjaxGetLoginItem(self):
		response = self.client.get('/ajax/getLoginItem/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'loginNavItem.html')
		self.assertTrue('csrf_token' in response.context)
		self.assertTrue('user' in response.context)
		self.assertTrue(response.context['user'].is_anonymous())





