# Generated by Django 2.1.4 on 2019-02-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booked_viewings',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile_no', models.CharField(max_length=10)),
                ('property_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact_on_property',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('message', models.CharField(max_length=1000)),
                ('property_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='listings_waiting_list',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('purpose', models.CharField(max_length=50)),
                ('tyype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='propety',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('property_title', models.CharField(max_length=2000)),
                ('location', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('property_type', models.CharField(max_length=50)),
                ('rent_buy', models.CharField(max_length=10)),
                ('property_picture', models.FileField(blank=True, upload_to='')),
                ('entrance_pic', models.FileField(blank=True, upload_to='')),
                ('sitting_pic', models.FileField(blank=True, upload_to='')),
                ('dining_pic', models.FileField(blank=True, upload_to='')),
                ('kitchen_pic', models.FileField(blank=True, upload_to='')),
                ('bedroom_pic', models.FileField(blank=True, upload_to='')),
                ('bathroom_pic', models.FileField(blank=True, upload_to='')),
                ('description', models.CharField(max_length=5000)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('patio', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('area', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('email', models.CharField(max_length=150)),
                ('subscriber_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
