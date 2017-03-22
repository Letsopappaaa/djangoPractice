from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	context = {
	"form" : form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save
		
	return render(request, 'post_form.html', context)

def post_edit(request):
	context = {
		
	}
	return render(request, 'post_form.html', context)

def post_list(request):
	queryset_list = Post.objects.all().order_by('-upload_time')

	context = {
		"queryset_list" : queryset_list,
	}
	return render(request, 'post_list.html', context)

def posts_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	headlines = Post.objects.all().filter(headlines=True).order_by('-upload_time')
	queryset_list = Post.objects.all().order_by('-upload_time')	
	context = {
	'instance' : instance,
	'headlines' : headlines,
	"queryset_list" : queryset_list,
	}
	return render(request, 'post_detail.html', context)

def post_delete(request):
	context = {
		
	}
	return redirect("posts:list")

def categories(request, hashtag):
	queryset_list = Post.objects.all().filter(hashtag=hashtag).order_by('-upload_time')
	headlines = Post.objects.all().filter(headlines=True).order_by('-upload_time')
	queryset_list_all = Post.objects.all().order_by('-upload_time')

	context={
	"queryset_list" : queryset_list,
	"queryset_list_all" : queryset_list_all,
	'headlines' : headlines,
	}
	return  render(request, 'categories.html', context)