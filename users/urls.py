from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from .views import custom_logout
from .views import edit_profile
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', custom_logout, name="Logout"),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('password-change/', PasswordChangeView.as_view(template_name='users/cambiar_contrasena.html', success_url='/users/password-change-done/'), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='users/cambiar_contrasena_done.html'), name='password_change_done'),
]