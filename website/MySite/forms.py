from django import forms
from bootstrap_datepicker.widgets import DatePicker
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
# from .models import Agent

from .models import subscriber
from .models import listings_waiting_list
from .models import propety


class subscribe_form(forms.ModelForm):
	class Meta:
		model = subscriber
		fields = '__all__'

class list_form(forms.ModelForm):
	class Meta:
		model = propety
		fields = '__all__'

from .models import contact_on_property

class customer_form(forms.ModelForm):
	class Meta:
		model = contact_on_property
		fields = ['message_id','message','name','email','property_id']

class DateInput(forms.DateTimeInput):
	input_type = 'date'

from .models import booked_viewings	
class booking_form(forms.ModelForm):
	class Meta:
		model = booked_viewings
		fields = '__all__'
		
class property_form(forms.ModelForm):
	description = forms.CharField( widget=forms.Textarea )
	location = forms.CharField(max_length=100)
	
	class Meta:
		model = propety
		fields = '__all__'

class ListToProperty_Form(forms.ModelForm):
	class Meta:
		model = listings_waiting_list
		fields = '__all__'

# from .models import client
# class clientsignup(UserCreationForm):
# 	class Meta(UserCreationForm.Meta):
# 		model = client
# 		fields = '__all__'

# 	@transaction.atomic
# 	def save(self):
# 		user = super().save(commit=False)
# 		user.is_client = True
# 		user.save()
# 		client = client.objects.create(user=user)
# 		return user
class searchform(forms.ModelForm):
	class Meta:
		model = propety
		fields = '__all__'