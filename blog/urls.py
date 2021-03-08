# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 00:06:26 2021

@author: bobby
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]