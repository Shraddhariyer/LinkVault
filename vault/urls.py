from django.urls import path
from . import views

urlpatterns = [
    path('links/', views.get_links),
    path('add-link/', views.add_link),
    path('delete-link/<int:id>/', views.delete_link),
    path('register/', views.register),
    path('login/', views.login),
]