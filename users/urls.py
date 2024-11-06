from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(template_name="users.html"), name='login'),
]