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
http://127.0.0.1:8000/risk/failedlogincountlastweek
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

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

