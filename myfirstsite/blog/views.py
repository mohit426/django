from django.shortcuts import render
from django.views.generic import ListView
from . import models
from django.shortcuts import render
# Create your views here.
# def post_list(request):
# 	return render(request, 'blogpost.html',{})
class HomePageView(ListView):
	model = models.Post
	template_name = 'blogpost.html'
	