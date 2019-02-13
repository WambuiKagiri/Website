# Generated by Django 2.1.4 on 2019-02-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0002_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('agent_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('profilepic', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
