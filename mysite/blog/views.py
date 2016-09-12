# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("This is Blog!")

# Create your views here.
