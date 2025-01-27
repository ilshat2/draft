from django.db import models
from django.contrib.auth.models import User


class UserAction(models.Model):
    """
    Модель, представляющая действия пользователей на платформе.

    Атрибуты:
        user (ForeignKey): Внешний ключ, связывающий действие с пользователем.
        action_type (CharField): Тип действия (например, "создание", "удаление").
        created_at (DateTimeField): Время, когда было выполнено действие. Автоматически присваивается текущее время при создании записи.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Строковое представление объекта UserAction.

        Возвращает строку в формате:
        'имя_пользователя - тип_действия at время_создания'.
        """
        return f'{self.user.username} - {self.action_type} at {self.created_at}'
