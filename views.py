from django.shortcuts import render
from draft.models import UserAction
from django.contrib.auth.models import User


def get_last_user_actions(request, user_id):
    """
    Получение списка последних действий пользователя.

    Этот метод извлекает последние 50 действий пользователя по его id из базы данных
    и передает их в шаблон для отображения.

    Аргументы:
        request: HTTP-запрос.
        user_id (int): Идентификатор пользователя для извлечения его действий.

    Возвращает:
        HTTP-ответ с рендером шаблона 'user_actions_list.html', который включает действия пользователя.
    """
    # Получаем пользователя по id
    user = User.objects.get(id=user_id)

    # Извлекаем последние 50 действий пользователя, отсортированных по времени создания
    actions = UserAction.objects.filter(user=user).order_by('-created_at')[:50]

    # Отправляем данные в шаблон для отображения
    return render(request, 'user_actions_list.html', {'actions': actions})
