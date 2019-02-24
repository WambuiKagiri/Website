from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import subscriber
from .models import listings_waiting_list
from .models import contact_on_property
from .models import propety
from .models import booked_viewings
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import Agent

admin.site.register(contact_on_property)
admin.site.register(booked_viewings)



class property_admin(admin.ModelAdmin):
	def formfield_for_dbfield(self, db_field, **kwargs):
		formfield = super(property_admin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'description':
			formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
			return formfield
		if db_field.name == 'location':
			formfield.widget = forms.TextInput(attrs=formfield.widget.attrs)
			return formfield
		if db_field.name == 'property_title':
			formfield.widget = forms.TextInput(attrs=formfield.widget.attrs)
			return formfield
		if db_field.name == 'price':
			formfield.widget = forms.TextInput(attrs=formfield.widget.attrs)
			return formfield
		if db_field.name == 'property_type':
			formfield.widget = forms.TextInput(attrs=formfield.widget.attrs)
			return formfield
		

	list_display = ['property_id','property_title','location','price','property_type','rent_buy','bedrooms','bathrooms','patio','garage','area']
	list_filter = ['price']
	class Meta:
		model = propety

class subAdmin(admin.ModelAdmin):
	list_display = ['subscriber_id','email']

	class Meta:
		model = subscriber


admin.site.register(subscriber,subAdmin)
admin.site.register(propety,property_admin)


class listings_waiting_listAdmin(admin.ModelAdmin):
	actions = ['add_to_properties']


	# def add_to_properties(self, request, queryset):
	# 	if 'do_action' in request.POST:
	# 		form = ListToProperty_Form(request.POST)
	# 		if form.is_valid():
		# admin.site.add_action(add_to_properties)

admin.site.register(listings_waiting_list,listings_waiting_listAdmin)


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = Agent
#     list_display = ['email', 'fname','lname','location','phone1','gender']

# admin.site.register(CustomUser, CustomUserAdmin)
