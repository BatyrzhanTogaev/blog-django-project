from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('create/', views.created_post, name='create_page'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_page'),
    path('post/<int:id>/detail', views.detail_post, name='detail_page'),
    path('post/<int:id>/delete', views.delete_post, name='delete')
]