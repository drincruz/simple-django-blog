from django.contrib import admin
from blog.models import Post, PostTag


class PostAdmin(admin.ModelAdmin):
    """
    Post admin customization
    """
    list_display = (
        'id', 'title',
        'publish_date', 'modified_date',
    )

admin.site.register(Post, PostAdmin)

class PostTagAdmin(admin.ModelAdmin):
    """
    PostTag admin customization
    """
    list_display = (
        'id',
        'tag',
        'post_title',
    )

    def post_title(self, obj):
        """
        Get the Post title of respective blog post
        """
        post = Post.objects.get(id=obj.post_id)
        return post.title

admin.site.register(PostTag, PostTagAdmin)
