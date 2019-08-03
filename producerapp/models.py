from django.db import models
import os


def generate_password():
    password=os.urandom(5).hex()
    return password


class StudentPro(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password=models.CharField(max_length=33,default=generate_password())


    class Meta:
        db_table='StudentPro'
