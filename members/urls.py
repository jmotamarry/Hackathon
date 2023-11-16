from django.urls import path, include

from . import views

# defines the different urls for the member app
urlpatterns = [
    path ('login_user/', views.login_user, name='login'),
    path ('logout_user/', views.logout_user, name='logout'),
    path ('register_user/', views.register_user, name='register_user'),
    path ('moderator/', views.moderator_view, name='moderator'),
    path ('moderator/update/<int:id>/', views.moderator_update_view),
    path ('moderator/delete/<int:id>/', views.moderator_delete_view),
    path ('moderator/view/<int:id>/', views.moderator_event_detail_view),
]