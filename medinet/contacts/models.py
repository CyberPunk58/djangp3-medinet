from django.db import models

class Contacts (models.Model):
    administration = 'Администрация'
    manager  = 'Менеджеры'
    siteadmins = 'Администраторы сайта'
    users = 'Пользователи'
    USERS_CHOICES = [
        (administration, 'Администрация'),
        (manager,'Менеджеры'),
        (siteadmins, 'Администраторы сайта'),
        (users, 'Пользователи'),
    ]



    full_name = models.CharField('ФИО', max_length=100)
    category = models.CharField(max_length=25, choices=USERS_CHOICES, default=users)
    job_title = models.CharField('Должность', max_length=50)
    ext_number = models.CharField('Внутренний телефон', max_length=5)
    phone_number = models.CharField('Городской телефон', max_length=12)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Номера телефонов'
        verbose_name_plural = 'Номера телефонов'
