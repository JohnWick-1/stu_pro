# Generated by Django 2.1 on 2019-08-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producerapp', '0006_auto_20190802_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpro',
            name='password',
            field=models.CharField(default='5c4a295e23', max_length=33),
        ),
    ]
