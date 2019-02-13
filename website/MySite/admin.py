from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render
from django import forms

from .models import subscriber
from .models import listings_waiting_list
from .models import contact_on_property
from .models import propety
from .models import booked_viewings


admin.site.register(contact_on_property)
admin.site.register(booked_viewings)



class property_admin(admin.ModelAdmin):
	def formfield_for_dbfield(self, db_field, **kwargs):
		formfield = super(property_admin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'description':
			formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
			return formfield

	list_display = ['property_id','property_title','location','price']
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


