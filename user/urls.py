from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', views.register_user, name='register_page'),
    path(
        'login/',
        LoginView.as_view(
            template_name='user/login_page.html',
            redirect_authenticated_user=True,
            next_page='home_page'),
        name='login_page'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile_user, name='profile_page')
]
