from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def client_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login')