from django.contrib import admin
from blog.models import Tag, Post


admin.site.register(Tag)
admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    