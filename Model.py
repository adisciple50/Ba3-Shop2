__author__ = 'Jason Crockett'

import django.db.models as datdb

class Item(datdb.Model):
    gid = datdb.AutoField(primary_key=True)
    name = datdb.CharField(max_length=60)
    image = datdb.ImageField(verbose_name="Product Picture")
    description = datdb.TextField(max_length=420)
    ebayURL = datdb.URLField()
    price = datdb.DecimalField(decimal_places=2)
    department = datdb.CharField(max_length=60)
    discount = datdb.IntegerField(default=0)
    dateadded = datdb.DateField(auto_created=1)

class User(datdb.Model):
    username = datdb.CharField(max_length=60,primary_key=True)
    email = datdb.EmailField()
    password = datdb.TextField()
    SecretQuestion = datdb.CharField(max_length=120)
    SecretQuestion = datdb.CharField(max_length=120)

