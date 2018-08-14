# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    published_at = models.DateTimeField(blank=True, null=True)

    # set published_at date
    def publish(self):
        self.published_at = timezone.now()
        self.save()

    # filter by approved_comments
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # redirect after creating Post instance
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(model.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    # approve comment
    def approve(self):
        self.approved_comment = True
        self.save()

    # redirect after comment
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
