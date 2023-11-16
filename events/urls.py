from django.urls import path
# importing the views we create
from .views import (
    event_detail_view, 
    event_create_view, 
    event_board_view, 
    event_delete_view, 
    event_update_view
)
                            # defines all of the paths for the events app
app_name = 'events'
urlpatterns = [
    path ('board/', event_board_view, name='board'),
    path ('<int:id>/', event_detail_view, name='event'),
    path ('create/', event_create_view, name='event_create'),
    path ('delete/<int:id>/', event_delete_view, name='event_delete'),
    path ('update/<int:id>/', event_update_view, name='event_update'),
]