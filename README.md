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

### Controllers

Requests are handled in controllers.py python file.

```
Give the example:
@csrf_exempt
def log(request):
    if request.method == 'POST' and request.FILES['logfile']:
        logfile = request.FILES['logfile']
        log_populate_service = LogPopulateService();
        log_populate_service.populate_log_into_risk_values_model(logfile)
        response = json.dumps([{'Success': "Risk Values are changed"}])
    else:
        response = json.dumps([{'Error': "Log file is must"}])
    return HttpResponse(response, content_type='text/json')
```

### Models

Models are defined in models.py python file.

* Each log row maps to instance of LogRow class 
```
class LogRow:
    def __init__(self, date, time, vm_name, vm_id, log_message):
        self.date = date
        self.time = time
        self.vm_name = vm_name
        self.vm_id = vm_id
        self.log_message = log_message
```

* Each log block maps to instance of LogBlock class. Such as login request etc.
```
class LogBlock:
    def __init__(self,vm_name,vm_id,date,time):
        self.vm_name = vm_name
        self.vm_id = vm_id
        self.date = date
        self.time = time
        self.log_rows = []

    def add_log_rows(self, log_row):
        self.log_rows.append(log_row)

    def post_complete_log_block(self):
        print(self.client_id)
```

* All log populate into RiskValuesModel class. Log Blocks are kept in a dictionary/map. This class is a singleton. 
And The class has caches of some requests so the App can respond quickly to some requests.
```
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class RiskValuesModel(metaclass=Singleton):
    def __init__(self):
        self.log_blocks_map = {}
        self.cache_is_user_known_map = {}
        self.cache_is_client_known_map = {}
        self.cache_is_ip_known_map = {}
    pass
```

### Services

Business logic is defined in services.py python file.

* Each log row maps to instance of LogRow class

### Backlog

* Cache system can be developed
* Log requests can be be queued
* Risk values requests can be queued

