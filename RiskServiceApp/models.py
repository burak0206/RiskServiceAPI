from django.db import models

class Person:
    def __init__(self, username, password):
        self.u = username
        self.p = password
