from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Post, PostAdmin)