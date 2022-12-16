from django.db import models

class Blanks(models.Model): # Модель для новостей на сайте
    title = models.CharField(max_length=200)  #Заголовок новости
    date = models.DateField()
    file = models.FileField(upload_to='blanks/files/')


    def __str__(self):
        return self.title