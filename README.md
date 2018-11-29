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
     .
     .
     .
```



## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

