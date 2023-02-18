from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('', authViews.LoginView.as_view(template_name='user/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='user/exit.html'), name='exit'),
]
