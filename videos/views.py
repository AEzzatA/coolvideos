from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Video

class VideosIndexView(ListView):
	model = Video

class VideoDetailView(DetailView):
	model = Video
	context_object_name = 'video'
