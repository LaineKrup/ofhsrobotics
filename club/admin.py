from django.contrib import admin

from .models import ContactMessage, Project, Resource


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'likes', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    list_filter = ('category',)
    search_fields = ('title', 'url')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'sent_at')
    readonly_fields = ('sent_at',)
    search_fields = ('name', 'message')
