# Generated by Django 2.1.4 on 2019-03-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0005_remove_booked_viewings_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_on_property',
            name='status',
            field=models.CharField(blank=True, choices=[('C', 'Complete'), ('P', 'Pending')], max_length=10),
        ),
        migrations.AddField(
            model_name='propety',
            name='agent',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]