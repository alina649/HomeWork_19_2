from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


from users.apps import UserConfig
from .views import RegisterView

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]