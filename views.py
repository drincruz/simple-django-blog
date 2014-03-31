"""
blog views

"""

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from blog.models import Post, PostTag
from blog.models import Comments

def index(request):
    """
    Blog index
    """
    ## Latest blog posts
    latest_blog_posts = Post.objects.filter(status='publish').order_by('-publish_date')[:3]

    return render_to_response(
        'blog/index.html',
        {
            'blogs': latest_blog_posts,
        }
    )

def archive(request):
    """
    Blog archive

    """
    ## Blog posts on index have 3 latest, so we'll show from the 3 latest on
    blog_posts = Post.objects.filter(status='publish').order_by('-publish_date')[3:]

    # Pagination
    paginator = Paginator(blog_posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render_to_response(
        'blog/archive.html',
        {
            'blogs': posts,
        }
    )

def post_perma(request, y, m, d, title):
    """
    Individual blog post permalinks
    """
    try:
        post = Post.objects.get(
            publish_date__year=y,
            publish_date__month=m,
            publish_date__day=d,
            slug=title,
        )
    except Post.DoesNotExist:
        raise Http404
    return render_to_response(
        'blog/post.html',
        {
            'post': post
        }
    )

def tagged_posts(request, searched_tag):
    """
    Blogs with tag
    """
    ## Get the post_id's of the PostTags with tag=searched_tag
    tag_post_ids = PostTag.objects.filter(tag=searched_tag).values_list('post_id')
    ## Get the posts with id in tag_post_ids
    blog_posts = Post.objects.filter(pk__in=tag_post_ids).order_by('-publish_date')
    return render_to_response(
        'blog/index.html',
        {
            'blogs': blog_posts
        }
    )
