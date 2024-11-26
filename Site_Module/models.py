from django.db import models


class SiteSetting(models.Model):
    is_main_setting = models.BooleanField(default=False, verbose_name=' تنظیم بعنوان تنظیمات اصلی سایت')
    logo = models.ImageField(upload_to='images/site_setting', verbose_name='لوگوی سایت', null=True, blank=True)
    team_name = models.CharField(max_length=150, verbose_name='نام تیم')
    copyright_text = models.TextField(verbose_name='متن کپی رایت')
    team_description = models.TextField(verbose_name='توضیحات درباره تیم')

    def __str__(self):
        return f'{self.team_name} | {self.is_main_setting}'

    class Meta:
        verbose_name = 'تنظیمات اصلی سایت'
        verbose_name_plural = 'تنظیمات اصلی سایت'
