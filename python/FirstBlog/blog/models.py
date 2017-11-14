# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

##from django.db import models
 
class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()



brew install mysql
easy_install mysql-python
 
mysqld_safe --skip-grant-tables #let anyone have full permissions
mysql -u root
UPDATE mysql.user SET Password=PASSWORD('nettuts') WHERE User='root'; #give the user 'root' a password
FLUSH PRIVILEGES;
 
mysql -u root -p #log in with our password 'nettuts'
CREATE DATABASE firstblog;
quit
 
python2.7 manage.py runserver
