from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from . import models
from django.http import JsonResponse
import time
# Create your views here.

#view for home page
def index(request):

    # get all objects from specific models
    musics = Music.objects.all()
    events = Event.objects.all()
    youtubeFeeds = YoutubeFeed.objects.all()
    contactInfo = ContactInfo.objects.all()

    context = {
        "musics" : musics,
        "events" : events,
        "youtubeFeeds" : youtubeFeeds,
        "contactInfo" : contactInfo
    }

    return render(request, 'index.html', context)

# view for about page
def about(request):

    # get all objects from specific models
    musics = Music.objects.all()
    events = Event.objects.all()
    youtubeFeeds = YoutubeFeed.objects.all()
    contactInfo = ContactInfo.objects.all()

    context = {
        "musics" : musics,
        "events" : events,
        "youtubeFeeds" : youtubeFeeds,
        "contactInfo" : contactInfo
    }

    return render(request, 'about.html', context)

# view for diecography page
def discography(request):

    # get all objects from specific models
    musics = Music.objects.all()
    events = Event.objects.all()
    youtubeFeeds = YoutubeFeed.objects.all()
    contactInfo = ContactInfo.objects.all()

    context = {
        "musics" : musics,
        "events" : events,
        "youtubeFeeds" : youtubeFeeds,
        "contactInfo" : contactInfo
    }

    return render(request, 'discography.html', context)

# view for videos page
def videos(request):

    # get all objects from specific models
    musics = Music.objects.all()
    events = Event.objects.all()
    youtubeFeeds = YoutubeFeed.objects.all()
    contactInfo = ContactInfo.objects.all()

    context = {
        "musics" : musics,
        "events" : events,
        "youtubeFeeds" : youtubeFeeds,
        "contactInfo" : contactInfo
    }

    return render(request, 'videos.html', context)

# view for contact page
def contact(request):

    # get all objects from specific models
    musics = Music.objects.all()
    events = Event.objects.all()
    youtubeFeeds = YoutubeFeed.objects.all()
    contactInfo = ContactInfo.objects.all()

    context = {
        "musics" : musics,
        "events" : events,
        "youtubeFeeds" : youtubeFeeds,
        "contactInfo" : contactInfo
    }

    return render(request, 'contact.html', context)

# view for completed success subscription
def newsletterTrue(request):
    newsletterObj = models.Newsletter()

    email = request.POST.get('email')

    newsletterObj.email = email
    newsletterObj.save()

    return render(request, 'newslettersubscriptionsuccess.html')

# view for sent message
def sentMessage(request):
    sentmessageObj = models.Message()

    name = request.POST.get('name')
    mail = request.POST.get('mail')
    website = request.POST.get('website')
    comment = request.POST.get('comment')

    sentmessageObj.name = name
    sentmessageObj.email = mail
    sentmessageObj.website = website
    sentmessageObj.comment = comment
    sentmessageObj.save()

    return render(request, 'sentsuccessful.html')