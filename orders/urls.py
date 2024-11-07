from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView


urlpatterns = [
    # path('add/', LoginView.as_view(template_name="users.html"), name='login'),
]