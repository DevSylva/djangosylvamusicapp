from django.contrib import admin
from .models import *
# Register your models here.

class YoutubeFeedAdmin(admin.ModelAdmin):
    """to help me display it in a cooler format"""
    list_display = ('description', 'image', 'link')


class MusicAdmin(admin.ModelAdmin):
    """to help me display it in a cooler format"""
    list_disply = ('artist', 'title', 'file_location')


class MessageAdmin(admin.ModelAdmin):
    """to help me display it in a cooler format"""
    list_display = ('name', 'email','time')


class VideoAdmin(admin.ModelAdmin):
    """to help me display it in a cooler format"""
    list_display = ('tag', 'link')


class EventAdmin(admin.ModelAdmin):
    """to help me display it in a cooler format"""
    list_display = ('name', 'event', 'date', 'location')


class ContactInfoAdmin(admin.ModelAdmin):
    """to help me display it in a cooler format"""
    list_display = ('email', 'phoneNumber', 'hotline', 'address')

class NewsletterAdmin(admin.ModelAdmin):
    """to help me display it in a cooler format"""
    list_display = ('email', 'time')

admin.site.register(YoutubeFeed, YoutubeFeedAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Newsletter, NewsletterAdmin)