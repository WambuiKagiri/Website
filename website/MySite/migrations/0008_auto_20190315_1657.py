# Generated by Django 2.1.4 on 2019-03-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0007_auto_20190315_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_on_property',
            name='status',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
