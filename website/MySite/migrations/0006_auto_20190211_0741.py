# Generated by Django 2.1.4 on 2019-02-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0005_contact_on_property_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked_viewings',
            name='property_id',
            field=models.IntegerField(),
        ),
    ]
