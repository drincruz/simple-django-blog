from django.db import models
from django.contrib import auth
from django.forms import ModelForm 
from django.template.defaultfilters import slugify
from datetime import datetime
import re
import string

class Post(models.Model):
    """
    Post data class represents a Blog Post
    """
    title = models.CharField(max_length=500)
    content = models.TextField()
    image_uri = models.CharField(max_length=500, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(auth.models.User)
    slug = models.SlugField(max_length=500, blank=True)
    status = models.CharField(
        max_length=7, choices=(('publish', 'publish'), ('draft', 'draft')), default='draft'
    )

    def __unicode__(self):
        return self.title

    def _get_permalink(self):
        """
        Returns the permalink
        """
        pub_date = self.publish_date
        return "{0}/{1}".format(self.publish_date.strftime('%Y/%m/%d'), self.slug)

    permalink = property(_get_permalink)

    def get_latest_posts(self, num_posts=3):
        return self.objects.order_by('publish_date').reverse[:num_posts]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
