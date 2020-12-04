from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('discography/', views.discography, name="discography"),
    path('videos/', views.videos, name="videos"),
    path('contact/', views.contact, name="contact"),
    path('newsletter/', views.newsletterTrue, name="newsletter"),
    path('messagesent/', views.sentMessage, name="sentmessage"),
]