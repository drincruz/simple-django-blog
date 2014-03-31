from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    # /blog/
    url(r'^$', views.index, name='index'),
    # /blog/archive/
    url(r'^archive/?$', views.archive, name='archive'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/(\w[^$]+)$', views.post_perma, name='post_perma'),
    url(r'^tag/(\w[^$]+)$', views.tagged_posts, name='tagged_posts'),
)
