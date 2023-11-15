from django.urls import path
from .views import (
    event_detail_view, 
    event_create_view, 
    event_board_view, 
    event_delete_view, 
    event_update_view
)

app_name = 'events'
urlpatterns = [
    path ('board/', event_board_view, name='board'),
    path ('<int:id>/', event_detail_view, name='event'),
    path ('create/', event_create_view, name='event_create'),
    path ('delete/<int:id>/', event_delete_view, name='event_delete'),
    path ('update/<int:id>/', event_update_view, name='event_update'),
]