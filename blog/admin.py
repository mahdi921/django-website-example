from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date', 'created_date', 'updated_date')
    list_filter = ('status','author', 'created_date')
    search_fields = ('title', 'content')
    # ordering = ['-created_date']
    actions = ['make_published']
    empty_value_display = '-empty-'
    date_hierarchy = 'created_date'

# admin.site.register(Post, PostAdmin)