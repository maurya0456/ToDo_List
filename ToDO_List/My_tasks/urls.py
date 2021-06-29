from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.delete_task, name='delete')
]
