__author__ = 'Jason Crockett'

import django.shortcuts.render as PageRender
from Model import Item
from Model import Department

def listDepartments(request):
    DepartmentsList = Department.listDepartments()
    return request(request,'Catagories.sk8',{'AllCategories':listDepartments()})

def listItemsByDepartment(request):
    department = request.GET.get('Department')
