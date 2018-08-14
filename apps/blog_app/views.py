# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Comment
# for CBV
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    # query on model
    def get_queryset(self):
        # grab posts that are LTE current time and list in desc order
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	redirect_field_name = 'blog_app/post_detail.html'
	form_class = PostForm

    model = Post



class PostUpdateView(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	redirect_field_name = 'blog_app/post_detail.html'
	form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
	login_url = '/login/'
	redirect_field_name = 'blog_app/post_list.html'

	model = Post

	def get_queryset(self):
		# can't have publication date
		return Post.objects.filter(published_at__isnull=True).order_by('created_at')
