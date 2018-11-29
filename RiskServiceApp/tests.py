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

    def test_populate_log(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            response = c.post('/log', {'logfile': fp})
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'Success': 'Risk Values are changed'}]
        )

    def test_is_user_know_when_username_not_exist(self):
        c = Client()
        response = c.get('/risk/isuserknown')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "username is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "username is must"}]
        )

    def test_is_user_know_when_username_exist_and_not_login(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isuserknown?username=admin')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is User Known?": false}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is User Known?": False}]
        )

    def test_is_user_know_when_username_exist_and_login(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isuserknown?username=cryptzone')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is User Known?": true}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is User Known?": True}]
        )

    def test_is_client_known_when_client_parameter_not_exist(self):
        c = Client()
        response = c.get('/risk/isclientknown')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "clientid is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "clientid is must"}]
        )

    def test_is_client_known_when_client_not_exists_in_log(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isclientknown?clientid=admin')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is ClientID Known?": false}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is ClientID Known?": False}]
        )

    def test_is_client_known_when_client_exists_in_log(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isclientknown?clientid=10.2.2dev_2014032715')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is ClientID Known?": true}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is ClientID Known?": True}]
        )

    def test_is_ip_known_when_ip_parameter_not_exist(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isipknown')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "ip is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "ip is must"}]
        )

    def test_is_ip_known_when_ip_not_exist_in_log(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isipknown?ip=192.168.101.5')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is IP Known?": false}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is IP Known?": False}]
        )

    def test_is_ip_known_when_ip_exist_in_log(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isipknown?ip=112.196.12.67')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is IP Known?": true}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is IP Known?": True}]
        )

    def test_is_ip_internal_when_ip_parameter_not_exist(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isipinternal')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "ip is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "ip is must"}]
        )

    def test_is_ip_internal_when_ip_is_internal(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isipinternal?ip=192.168.101.5')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is IP Internal?": true}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is IP Internal?": True}]
        )

    def test_is_ip_internal_when_ip_is_external(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/isipinternal?ip=162.158.89.41')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Is IP Internal?": false}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Is IP Internal?": False}]
        )

    def test_last_successful_login_date_when_username_parameter_not_exist(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/lastsuccessfullogindate')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "username is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "username is must"}]
        )

    def test_last_successful_login_date_when_username_not_login(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/lastsuccessfullogindate?username=admin')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "User has not never logged"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "User has not never logged"}]
        )

    def test_last_successful_login_date_when_username_login(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/lastsuccessfullogindate?username=test_rs')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"datetime": "2014-06-17T14:54:54"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"datetime": "2014-06-17T14:54:54"}]
        )

    def test_last_failed_login_date_when_username_parameter_not_exist(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/lastfailedlogindate')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "username is must"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "username is must"}]
        )

    def test_last_failed_login_date_when_username_not_login(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/lastfailedlogindate?username=admin')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"datetime": "2014-06-17T22:40:02"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"datetime": "2014-06-17T22:40:02"}]
        )

    def test_last_failed_login_date_when_username_can_not_login(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/lastfailedlogindate?username=test_rs')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"Error": "There is no that User can not login"}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"Error": "There is no that User can not login"}]
        )

    def test_failed_login_count_last_week(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/failedlogincountlastweek')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"count": 0}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"count": 0}]
        )

    def test_failed_login_count_520_weeks_ago(self):
        c = Client()
        with open('Python Programming Task - Sample Logs.txt') as fp:
            c.post('/log', {'logfile': fp})
        response = c.get('/risk/failedlogincountlastweek?weeks=520')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '[{"count": 493}]')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"count": 493}]
        )

#/risk/failedlogincountlastweek

#/risk/failedlogincountlastweek?weeks=520