from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('statuses/', views.statuses, name='statuses'),
    path('subcategories/', views.subcategories, name='subcategories'),
    path('types/', views.types, name='types'),
    path('statuses/add_status/', views.add_status),
    path('statuses/delete/<int:id>/', views.delete_status),
    path('statuses/edit/<int:id>/', views.edit_status),
    path('types/add_type/', views.add_type),
    path('types/edit_type/<int:id>/', views.edit_type),
    path('types/delete_type/<int:id>/', views.delete_type),
    path('categories/add_category/', views.add_category),
    path('categories/edit_category/<int:id>/', views.edit_category),
    path('categories/delete_category/<int:id>', views.delete_category),
    path('subcategories/add_subcategory/', views.add_subcategory),
    path('subcategories/edit_subcategory/<int:id>/', views.edit_subcategory),
    path('subcategories/delete_subcategory/<int:id>/', views.delete_subcategory),
    path('new_dds/', views.to_add_dds, name='add_dds'),
    path('new_dds/add_dds', views.add_dds),
    path('edit_dds/<int:id>/', views.edit_dds),
    path('delete_dds/<int:id>/', views.delete_dds),
]