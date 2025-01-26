from django.shortcuts import render
from draft.models import UserAction
from django.contrib.auth.models import User


def get_last_user_actions(request, user_id):
    user = User.objects.get(id=user_id)  # Получаем пользователя по id
    actions = UserAction.objects.filter(user=user).order_by('-created_at')[:50]
    return render(request, 'user_actions_list.html', {'actions': actions})
