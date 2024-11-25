from django.urls import path

from . import post_views

urlpatterns = [
    path('',post_views.index,name = 'index'),

]