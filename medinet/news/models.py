from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model): # Модель для новостей на сайте
    title = models.CharField(max_length=200)  #Заголовок новости
    #description = models.CharField(max_length=300) #Описание новости
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='news/images/')
    url = models.URLField(blank=True) #Для ссылок Blank - открывает ссылкив новом окне


    def __str__(self):
        return self.title