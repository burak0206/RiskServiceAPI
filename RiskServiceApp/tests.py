# Create your tests here.
from django.test import SimpleTestCase
from django.test import Client


class RiskServiceApiTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        c = Client()
        response = c.get('/risk/isuserknown')
        print(response)
        print(response.content)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "username is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "username is must"}]
        )
