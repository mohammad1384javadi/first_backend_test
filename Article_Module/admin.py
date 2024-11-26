from django.contrib import admin
from django.http import HttpRequest

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'author', 'is_active']
    list_filter = ['is_active', 'author', 'create_date']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
