from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from .views import custom_logout

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    # path('logout/', LogoutView.as_view(template_name='appventas/padre.html'), name="Logout")
    # path('logout/', LogoutView.as_view(next_page='inicio'), name="Logout"),
    path('logout/', custom_logout, name="Logout"),
]