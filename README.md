# Risk Service API

In this report, the technologies, endpoints, test cases, classes, functions and backlogs will be explained.

### The Technologies

Python 3.6 and Django 2.1.3 are used to build the project.

### Endpoints

```
http://localhost:8000/log
http://localhost:8000/log/clear
http://localhost:8000/risk/isuserknown?username=UserA
http://localhost:8000/risk/isclientknown?clientid=fe80::84c:15f9:f9f5:12c3
http://localhost:8000/risk/isipknown?ip=192.168.101.5
http://localhost:8000/risk/isipinternal?ip=192.168.101.5
http://localhost:8000/risk/lastsuccessfullogindate?username=test_rs
http://localhost:8000/risk/lastfailedlogindate?username=admin
http://localhost:8000/risk/failedlogincountlastweek
```

### Test Cases

22 test cases are implemented. I used SimpleTestCase which is from django.test.

```
Give the example:

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
     .
     .
     .
```




### Backlog

* Cache system can be developed
* Log requests can be be queued
* Risk values requests can be queued

