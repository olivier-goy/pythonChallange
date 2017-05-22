# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    def __str__(self):
        return self.first_name + " " + self.name + " " + str(self.age)
