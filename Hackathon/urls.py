"""Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.urls

from pages.views import home_view
from events.views import event_board_view

# sets the main paths
urlpatterns = [
    path ('event/', include('events.urls')),                        # check all the urls in the events app with an event/
    path ('members/', include('members.urls')),                     # check in members app with members/
    path ('members/', include('django.contrib.auth.urls')),
    path ('', event_board_view, name='home'),                       # home url
    path ('admin/', admin.site.urls),                               # django admin
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # needed to take in images