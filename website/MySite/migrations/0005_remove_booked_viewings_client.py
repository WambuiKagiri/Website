# Generated by Django 2.1.4 on 2019-03-15 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0004_auto_20190315_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked_viewings',
            name='client',
        ),
    ]
