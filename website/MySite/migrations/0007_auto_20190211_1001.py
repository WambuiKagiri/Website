# Generated by Django 2.1.4 on 2019-02-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0006_auto_20190211_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked_viewings',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='listings_waiting_list',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
    ]
