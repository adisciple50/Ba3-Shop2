__author__ = 'Jason Crockett'

import django.db.models as datdb
import django.db.models.manager as dbiface
import django.forms.formsets as dbiform

class Item(datdb.Model):
    iid = datdb.AutoField(primary_key=True)
    name = datdb.CharField(max_length=60)
    image = datdb.ImageField(verbose_name="Product Picture")
    description = datdb.TextField(max_length=420)
    ebayURL = datdb.URLField()
    price = datdb.DecimalField(decimal_places=2)
    department = datdb.CharField(max_length=60)
    discount = datdb.IntegerField(default=0)
    dateadded = datdb.DateField(auto_created=1)
    ItemSlug = datdb.SlugField()

    def listItemsByDepartment(self,Department):
        ItemsInDepartment = dbiface.QuerySet(Item).filter(Department)
        return ItemsInDepartment

    def getUniqueDepartments(self):
        UniqueDepartments = dbiface.QuerySet(Item.department).distinct()
        return UniqueDepartments

    def returnItemsByQuery(self):
        requestedItem = dbiform.Form(self.name)
        return dbiface.QuerySet(Item,Item_name_contains=requestedItem)

class User(datdb.Model):
    iid = datdb.AutoField()
    username = datdb.CharField(max_length=60,primary_key=True)
    email = datdb.EmailField()
    password = datdb.TextField()
    SecretQuestion = datdb.CharField(max_length=120)
    SecretAnswer = datdb.CharField(max_length=120)

class Department(datdb.Model):
    iid = datdb.AutoField()
    department = datdb.CharField(max_length=60,primary_key=True)
    ReductionByPercent = datdb.DecimalField()
    ReductionByCash = datdb.DecimalField()
    RiseByPercent = datdb.DecimalField()
    RiseByCash = datdb.DecimalField()
    ReducePrice = datdb.NullBooleanField()
    IncreasePrice = datdb.NullBooleanField()
    ApplyTax = datdb.BooleanField()
    Tax = datdb.DecimalField()
    def listDepartments(self):
        return self.department.column()

    def update(self):
        dataDelete = dbiface.QuerySet(self.department).delete()
        dbiface.QuerySet(self.department).bulk_create(Item.getUniqueDepartments())
        self.update()



