from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('create', views.created_post, name='create_page'),
] 