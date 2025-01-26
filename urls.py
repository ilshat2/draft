from django.urls import path
from draft import views


urlpatterns = [
    path('user/<int:user_id>/actions/', views.get_last_user_actions, name='user_actions')
]
