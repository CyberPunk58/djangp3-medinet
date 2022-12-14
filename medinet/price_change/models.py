from django.db import models

class Price_change(models.Model):
    title = models.CharField(max_length=200)  #Заголовок изменения
    description = models.TextField(default="default title") #Описание изменения
    date = models.DateField()
    file = models.FileField(upload_to='price_change/files/')


    def __str__(self):
        return self.title