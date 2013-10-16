from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from blog.models import Post
from blog.models import Comments

def index(request):
    """
    Blog index
    """
    latest_blog_posts = Post.objects.order_by('-publish_date')[:3]
    return render_to_response(
        'blog/index.html',
        {'recent_blogs': latest_blog_posts}
    )

def post_perma(request, y, m, d, title):
    """
    Individual blog post permalinks
    """
    post = Post.objects.get(
        publish_date__year=y,
        publish_date__month=m,
        publish_date__day=d,
        slug=title,
    )
    return render_to_response('blog/post.html', {'post': post})
