from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import generic
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth import login as clogin
from django.contrib.auth import authenticate
from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test
from ajax_search.forms import SearchForm

import json
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
	)

user = get_user_model()
#imported forms
from .forms import subscribe_form
from .forms import list_form
from .forms import customer_form
from .forms import booking_form

#imported models
from .models import subscriber
from .models import listings_waiting_list
from .models import contact_on_property
from .models import booked_viewings
from .models import propety
from .models import Agent


import re

from django.db.models import Q

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

@csrf_protect
@ensure_csrf_cookie
def home( request, **kwargs):
	propertys = propety.objects.all().filter(rent_buy='Rent')[:4]
	props = propety.objects.all().filter(rent_buy='Buy')[:4]
	propetys = propety.objects.all()
	return render(request, 'index.html', {'propertys':propertys,'props':props, 'propetys':propetys})


@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
def subscribe(self, request, **kwargs):
	if request.method == 'POST':
		form = subscribe_form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your message has been sent")
			return HttpResponseRedirect('/')

		else:
			return HttpResponseRedirect('/')
				

	else:
		return render(request, 'properties.html', {'form':form})

def search(request):
   query_string = ''
   found_entries = ''
   if ('q' in request.GET) and request.GET['q'].strip():
	   query_string = request.GET['q']
	   entry_query = get_query(query_string, ['purpose', 'rent_buy', 'location'])
	   found_entries = propety.objects.filter(entry_query)
	   
	   return render_to_response('searchresults.html',{ 'query_string': query_string, 'found_entries': found_entries },context_instance=RequestContext(request))
	

class AboutPageView(TemplateView):
	def get(self, request, **kwargs): 
		return render(request, 'about.html', context=None)
		
class ContactPageView(TemplateView):
	def get(self, request, **kwargs): 
		return render(request, 'contact.html', context=None)

	def post(self,request, **kwargs):
		if request.method == 'POST':
			form = customer_form(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/success/')

		else:
			return render(request, 'success.html', {'form':form})	

# class ListPropertyPageView(TemplateView):
# 	def get(self, request, **kwargs): 
# 		return render(request, 'ListProperty.html', context=None)
@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Client').exists())
def listproperty(self,request, **kwargs):
	if request.method == 'POST':
		form = list_form(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'MySite/ListProperty.html', {'form':form})
				

		else:
			return render(request, 'ListProperty.html', {'form':form})

	else:
		return render(request, 'ListProperty.html', {'form':form})

	
	


class PropertyPageView(TemplateView):
	def get(self, request, property_title,pk, **kwargs): 
		propertys = propety.objects.all().filter(property_title= property_title)
		return render(request, 'property.html', {'propertys':propertys})

	
	@csrf_protect
	@ensure_csrf_cookie
	@login_required(login_url='/accounts/login/')		
	def post(self, request,**kwargs):
		if request.method == 'POST':
			form = customer_form(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, "Your message has been sent")
				return render(request,'property.html')

			else:
				return render(request, 'login.html')

		else:
			redirect('/property/')

	def post(self, request, **kwargs):
		if request.method == 'POST':
			form = booking_form(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/')
			
			else:
				render(request,'property.html', {'form':form})

class PropertiesPageView(TemplateView):
	def get(self, request, **kwargs):
		propertyss = propety.objects.all()
		paginator = Paginator(propertyss,4)
		

		page =request.GET.get('page')
		try:
			propertyss = paginator.page(page)
		except PageNotAnInteger:
			propertyss = paginator.page(1)
		except EmptyPage:
			propertyss = paginator.page(paginator.num_pages)

		return render(request, 'properties.html', {'propertyss':propertyss})

@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Agents').exists())
def dashboard(request):
	listt = listings_waiting_list.objects.all()
	books = booked_viewings.objects.all()
	paginator = Paginator(listt,8)
	
	page = request.GET.get('page')
	try:
		listt = paginator.page(page)
		
	except PageNotAnInteger:
		listt = paginator.page(1)
	except EmptyPage:
		listt = paginator.page(paginator.num_pages)
	
	return render(request, 'agent.html',{'listt':listt,'books':books})
	# else:
	# 	return redirect('/accounts/login/')

class ListingsPageView(TemplateView):
	def get(self,request, **kwargs):
		listt = listings_waiting_list.objects.all()
		paginator = Paginator(listt,8)

		page = request.GET.get('page')
		try:
			listt = paginator.page(page)
		except PageNotAnInteger:
			listt = paginator.page(1)
		except EmptyPage:
			listt = paginator.page(paginator.num_pages)

		return render(request,'requestedlistings.html',{'listt':listt})

class BookingsPageView(TemplateView):
	def get(self,request, **kwargs):
		books = booked_viewings.objects.all()	
		return render(request,'bookedviewings.html',{'books':books})


def chatindex(request):
    return render(request, 'chatindex.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def message(request, **kwargs):	
	return render(request,'message.html',context=None)


def agentprofile(request):
    return render(request,'profile.html')

def agentsearch(request):
	if request.method=="GET":
		search_text = request.POST['search_text']
	else:
		search_text = ''


	bookings =  booked_viewings.objects.all().filter(Title__icontains=search_text)[:5]
	listings =  listings_waiting_list.objects.all().filter(Title__icontains=search_text)[:5]

	return render(request,'agentsearch.html',{'bookings':bookings,'listings':listings})