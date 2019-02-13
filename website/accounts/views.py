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
from .forms import loginform




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
                return HttpResponseRedirect('/agent/')
            if user.groups.filter(name='Clients').exists():
                return HttpResponseRedirect('/')
                
        else:
            return render(request, 'registration/login.html',{"form":form})
                
    else:
        form =loginform()
        args = {'form':form}
        args.update(csrf(request))
        args['form'] = loginform
        return render(request,'registration/login.html',args)