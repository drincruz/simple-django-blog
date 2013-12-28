from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/(\w[^$]+)$', views.post_perma, name='post_perma'),
    url(r'^tag/(\w[^$]+)$', views.tagged_posts, name='tagged_posts'),
)
