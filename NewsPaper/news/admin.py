from django.contrib import admin
from .models import Post, Category, Source, PostCategory

admin.site.register(Post)

admin.site.register(Category)

admin.site.register(Source)

admin.site.register(PostCategory)
