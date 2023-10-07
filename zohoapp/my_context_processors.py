from .models import *
from django.shortcuts import render,redirect,get_object_or_404

def base_setting(request):
    return{
        "setting_variable":setting_list.objects.get(id=2),
    }