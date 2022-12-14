from django.db import models

class News(models.Model): # Модель для новостей на сайте
    title = models.CharField(max_length=200)  #Заголовок новости
    description = models.CharField(max_length=300) #Описание новости
    image = models.ImageField(upload_to='news/images/')
    url = models.URLField(blank=True) #Для ссылок Blank - открывает ссылкив новом окне


    def __str__(self):
        return self.title