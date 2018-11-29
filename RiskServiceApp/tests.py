# Create your tests here.
from django.test import SimpleTestCase
from django.test import Client


class RiskServiceApiTests(SimpleTestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{}]
        )

    def test_is_user_know_when_username_not_exist(self):
        c = Client()
        response = c.get('/risk/isuserknown')
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "username is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "username is must"}]
        )
