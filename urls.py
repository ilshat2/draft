from django.urls import path
from draft import views

urlpatterns = [
    # URL-путь для получения списка действий пользователя по его id
    path('user/<int:user_id>/actions/', views.get_last_user_actions, name='user_actions')
]
