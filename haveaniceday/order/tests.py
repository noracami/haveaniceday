from django.test import TestCase
from .models import Member

# Create your tests here.
class OrderViewTests(TestCase):
    def test_order_view(self):
        response = self.client.get('/order/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/home.html')

class MemberViewTests(TestCase):
    def setUp(self):
        member = Member(
            kmID='AB123456', edocID='edoc', emailID='abc', name='捕夢網',
            location='A局-B分局-C所', title='代理執行秘書')
        member.save()
        another_member = Member(
            name='test')
        another_member.save()

    def tearDown(self):
        Member.objects.all().delete()

    def test_member_view(self):
        r = self.client.get('/order/member/?id=1')
        self.assertContains(r, 'AB123456')

    def test_member_all(self):
        r = self.client.get('/order/member/all/')
        self.assertContains(r, 'test')
        self.assertContains(r, 'abc')
