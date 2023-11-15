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

from pages.views import home_view
from events.views import event_detail_view, event_create_view, event_board_view, event_delete_view

urlpatterns = [
    path ('', home_view, name='home'),
    path ('board/', event_board_view, name='board'),
    path ('event/<int:id>/', event_detail_view, name='event'),              # re_path with .* allows event/ with anything after
    path ('event/create/', event_create_view, name='event_create'),
    path ('event/delete/<int:id>/', event_delete_view, name='event_delete'),
    path ('admin/', admin.site.urls),
]
