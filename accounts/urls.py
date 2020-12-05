from django.urls import path
from . import views



urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout_req', views.logout_req, name='logout_req'),
]
