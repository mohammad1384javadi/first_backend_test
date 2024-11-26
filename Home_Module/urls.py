from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('about_us', views.AboutUsView.as_view(), name='about_us_page')
]