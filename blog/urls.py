# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:56:56 2020

@author: jgrippon
"""

from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]