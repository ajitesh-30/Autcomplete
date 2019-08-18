from django.contrib import admin
from django.urls import path,include
from .views import WordSearchView

urlpatterns = [
    path('search/',WordSearchView.as_view(),name='all-words'),
]