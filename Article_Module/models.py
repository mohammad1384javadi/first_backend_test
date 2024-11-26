from django.db import models

from Account_Module.models import User


class Article(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان مقاله')
    url_title = models.CharField(max_length=400, verbose_name='عنوان در url', unique=True)
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', editable=False)
    description = models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
