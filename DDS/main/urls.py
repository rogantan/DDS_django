from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('statuses/', views.statuses, name='statuses'),
    path('subcategories/', views.subcategories, name='subcategories'),
    path('types/', views.types, name='types'),
]