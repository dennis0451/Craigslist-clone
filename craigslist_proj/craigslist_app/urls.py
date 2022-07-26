from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('categories', views.all_cats, name='all_categories' ),
    path('categories/<int:category_id>/view', views.view_category,name='view_category'),
    path('categories/<int:category_id>/edit', views.edit_category,name='edit_category'),
    path('categories/<int:category_id>/delete', views.delete_category,name='delete_category'),
    path('categories/new', views.create_category, name='new_category'),
    path('posts', views.all_posts, name='all_posts'),
    path('posts/<int:post_id>', views.single_post, name='single_post'),
    path('categories/<int:category_id>/posts/new', views.create_post,name='new_post'),
    path('categories/<int:category_id>/posts/<int:post_id>',views.view_post, name='view_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/edit',views.edit_post, name='edit_post'),
    # path('posts/<int:post_id>', views.view_post, name='view_post'),


    # path('categories/<int:category_id>/edit', views.list, name='view_category'),

]

# python manage.py runserver --insecure
