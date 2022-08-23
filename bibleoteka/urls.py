from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]