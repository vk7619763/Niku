import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'table_demo.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()

'''def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
'''

def populate(n):
    for i in range(n):
        fname=fake.name()
        fcity=fake.city()
        fno=randint(1000,5000)
        fsal=randint(10000,50000)
        employee.objects.get_or_create(ename=fname,ecity=fcity,eno=fno,esal=fsal)

populate(25)
