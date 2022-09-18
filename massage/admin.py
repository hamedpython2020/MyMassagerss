from django.contrib import admin

# Register your models here.
from massage.models import Post, viewer

admin.site.register(Post)
admin.site.register(viewer)