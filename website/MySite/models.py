from django.db import models
from django.forms import ModelForm
from django.contrib import admin

# Create your models here.
class subscriber(models.Model):
	email = models.CharField(max_length=150)
	subscriber_id = models.AutoField(primary_key=True)

class contact_on_property(models.Model):
	message_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=150)
	message = models.CharField(max_length=1000)
	

class listings_waiting_list(models.Model):
	property_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	mobile_no = models.IntegerField()
	location = models.CharField(max_length=100)
	price = models.IntegerField()
	purpose = models.CharField(max_length=50)
	tyype = models.CharField(max_length=50)

	

class booked_viewings(models.Model):
	booking_id = models.AutoField(primary_key=True)
	mobile_no = models.IntegerField()
	property_id = models.IntegerField(blank=True)
	name = models.CharField(max_length=100)
	date = models.DateField(blank=False,)

class property(models.Model):
	property_id = models.AutoField(primary_key=True)
	property_title = models.CharField(max_length=2000)
	location = models.CharField(max_length=1000)
	price = models.IntegerField()
	property_type = models.CharField(max_length=50)
	rent_buy = models.CharField(max_length=10)
	property_picture = models.FileField(upload_to='',blank=True)
	entrance_pic = models.FileField(upload_to='',blank=True)
	sitting_pic = models.FileField(upload_to='',blank=True)
	dining_pic = models.FileField(upload_to='',blank=True)
	kitchen_pic = models.FileField(upload_to='',blank=True)
	bedroom_pic = models.FileField(upload_to='',blank=True)
	bathroom_pic = models.FileField(upload_to='',blank=True)
	description = models.CharField(max_length=5000)
	bedrooms = models.IntegerField()
	bathrooms = models.IntegerField()
	patio = models.IntegerField()
	garage = models.IntegerField()
	area = models.CharField(max_length=20,blank=True)


from .forms import property_form

class property_admin(admin.ModelAdmin):
	form = property_form
	