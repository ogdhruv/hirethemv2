from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "created"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "created"
    fieldsets = (
        ("Title options", {
            'fields': ('title', 'slug', 'author')
        }),
        ('Main options', {
            'fields': ('body', 'tags'),
        }),
        ('Regarding dates', {
            'classes': ('collapse',),
            'fields': ('created', 'updated'),

        })
    )
    ordering = ["created", "updated"]
