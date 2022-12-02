from django.contrib import admin
from .models import Room, Message

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "updated", "created"]
    search_fields = ["title", "description"]
    raw_id_fields = ["host"]
    date_hierarchy = "created"
    ordering = ["created", "updated"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["user", "room", "created"]
    search_fields = ["room"]
    date_hierarchy = "created"
    readonly_fields = ["created"]
    ordering = ["created"]
