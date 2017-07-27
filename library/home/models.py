# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here. 

class book_entry(models.Model):

    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
   
    def __str__(self):
        return self.name



    
    
