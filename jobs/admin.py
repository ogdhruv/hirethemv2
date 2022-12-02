from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Company, Job


# Register your models here.
@admin.register(Job)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "host","location","created"]
    search_fields = ["title","tags","location"]
    date_hierarchy = "created"
    ordering = ["created"]
    fieldsets = (
        (_("Job info"), {"fields": ("title", "host","location","company")}),
        (_("Job description"),{"fields": ("description", "type","last_date","salary")}),
        (_("Additional"),{"fields":("form_link","tags")})
    )


@admin.register(Company)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "website"]
    search_fields = ["name", "website"]
    date_hierarchy = "created"
    ordering = ["created"]
    fieldsets = (
        (_("Company info"), {"fields": ("name", "website")}),
        (_("Company description"),{"fields": ("logo", "description")}),
    )


# @admin.register(Applicant)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ["user", "status", "created"]
#     search_fields = ["user"]
#     date_hierarchy = "created"
#     ordering = ["created"]
