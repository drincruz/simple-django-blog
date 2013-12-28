from django import template
from django.utils.safestring import mark_safe 
from blog.models import PostTag

register = template.Library()

@register.filter(name='get_tags', needs_autoescape=True)
def get_tags(p_id, autoescape=None):
    """
    Get the tags from a post
    """
    tags = PostTag.objects.filter(post_id=p_id)
    tag_links = []
    for t in tags:
        tag_links.append("<a href=\"/blog/tag/"+t.tag+"\">"+t.tag+"</a>")
    if 0 < len(tag_links) and autoescape:
        return mark_safe(", ".join(tag_links))
    else:
        return mark_safe("")
