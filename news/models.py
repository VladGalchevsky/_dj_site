from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва')
    content = models.TextField(verbose_name='Вміст')
    create_at = models.DateTimeField(auto_now_add=True, 
                                     verbose_name='Створено')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото',
                              blank=True)
    is_published = models.BooleanField(default=True, 
                                       verbose_name='Опубліковано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, 
                                 verbose_name='Категорія', null=True)


    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-create_at'] 
        

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, 
                             verbose_name='Назва')

    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']