from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/users', verbose_name='پروفایل', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی حساب کاربری')
    is_dev = models.BooleanField(
        default=False,
        verbose_name='توسعه دهنده سایت',
        help_text='نشان میدهد این کاربر این سایت را طراحی کرده است یا خیر.'
    )
    field = models.CharField(
        max_length=500,
        verbose_name='فیلد کاری',
        help_text='مشخص میکند کاربر توسعه دهنده در چه فیلدی مشغول کار است',
        null=True,
        blank=True)
    # skill = models.ManyToManyField(
    #     'DeveloperSkills',
    #     verbose_name='مهارت ها',
    #     related_name='user_skills',
    #     null=True,
    #     blank=True
    # )
    skill = models.TextField(verbose_name='مهارت ها', null=True, blank=True)

    def __str__(self):
        if self.last_name is not '' and self.first_name is not '':
            return self.get_full_name()
        else:
            return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


# class DeveloperSkills(models.Model):
#     user = models.ForeignKey(User, verbose_name='کاربر', null=True, on_delete=models.CASCADE)
#     skill = models.CharField(max_length=300, verbose_name='مهارت', help_text='مشخص کننده مهارت توسعه دهنده است')
#
#     def __str__(self):
#         return self.skill
#
#     class Meta:
#         verbose_name = 'مهارت'
#         verbose_name_plural = 'مهارت ها'
