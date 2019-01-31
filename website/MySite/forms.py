from django import forms
from bootstrap_datepicker.widgets import DatePicker

from .models import subscriber
from .models import listings_waiting_list
from .models import contact_on_property
from .models import booked_viewings,property

class subscribe_form(forms.ModelForm):
	class Meta:
		model = subscriber
		fields = '__all__'

class list_form(forms.ModelForm):
	class Meta:
		model = listings_waiting_list
		fields = ['property_id','name','mobile_no','location','price','purpose','tyype']

class customer_form(forms.ModelForm):
	class Meta:
		model = contact_on_property
		fields = '__all__'

class booking_form(forms.ModelForm):
	class Meta:
		model = booked_viewings
		fields = '__all__'
		
class property_form(forms.ModelForm):
	description = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = property
		fields = '__all__'

class ListToProperty_Form(forms.ModelForm):
	class Meta:
		model = listings_waiting_list
		fields = '__all__'
