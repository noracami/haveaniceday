from django.test import TestCase
from .models import TableOfMonth

# Create your tests here.
class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website_component/home.html')

class TableOfMonthViewTests(TestCase):
    """docstring for TableOfMonthViewTests"""
    def setUp(self):
        TableOfMonth.objects.create(author='AA12BB34', date='2016-03-01')

    def tearDown(self):
        TableOfMonth.objects.all().delete()

    def test_list_view(self):
        r = self.client.get('/table/')
        self.assertContains(
            r, '<a class="navbar-brand" href="/">Dashboard</a>',
            html=True,
        )
        self.assertContains(r, '<a href="/table/1/">2016年3月份輪值表</a>', html=True)
