from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined', 'is_active']
    list_filter = ['is_active', 'date_joined']
    list_editable = ['is_active']


admin.site.register(models.User, UserAdmin)
# admin.site.register(models.DeveloperSkills)
