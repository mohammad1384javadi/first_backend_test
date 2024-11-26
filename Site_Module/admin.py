from django.contrib import admin
from . import models


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'team_name', 'is_main_setting']
    list_editable = ['team_name']
    list_filter = ['is_main_setting']


admin.site.register(models.SiteSetting, SiteSettingAdmin)
