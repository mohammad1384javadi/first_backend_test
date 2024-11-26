from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Article


class ArticleListView(ListView):
    template_name = 'Article_Module/article_list.html'
    model = Article
    context_object_name = 'articles'
