from __future__ import unicode_literals
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
from django.contrib.auth import authenticate
from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test
import json
from django import forms
# Create your views here.
from .forms import loginform,RegistrationForm
from django.contrib.auth import get_user_model
user = get_user_model()




@csrf_protect
@ensure_csrf_cookie
def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            

            if user.groups.filter(name='Agents').exists():
                return render(request, 'agent.html')
            if user.groups.filter(name='Client').exists():
                return render(request, 'ListProperty.html')
                
        else:
            return render(request, 'registration/login.html',{"form":form})
                
    else:
        form =loginform()
        args = {'form':form}
        args.update(csrf(request))
        args['form'] = loginform
        return render(request,'registration/login.html',args)


@csrf_protect
@ensure_csrf_cookie
def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)  
		if form.is_valid():
			user = (form.save(commit=False))
			user.is_active = False
			user.save()
			group = form.cleaned_data.get('group')
			user.groups.add(Client)
			return HttpResponse('Please confirm your email address to complete the registration')
		else:
			return render(request,'registration/signup.html',{"form":form})

	else:
		form =RegistrationForm()
		args = {'form':form}
		args.update(csrf(request))
		args['form'] = RegistrationForm()
	return render(request,'registration/signup.html')

@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
# @user_passes_test(lambda u: u.groups.filter(name='Client').exists())
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

