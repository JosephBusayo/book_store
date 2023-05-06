from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_book', views.add_book, name='add_book'),
    path('update_book/<str:pk>/', views.update_book, name='update_book'),
    path('delete_book/<str:pk>/', views.delete_book, name='delete_book'),
    path('more_detail/<str:pk>/', views.more_detail, name='more_detail')
]
