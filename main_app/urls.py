from django.urls import path
from . import views
from .models import Widget


urlpatterns = [
  
    path('widgets/', views.widgets, name="widgets"),
    path('widgets/add', views.add_widget, name="add_widget"),
    path('widgets/delete/<int:pk>/', views.delete, name="widgets_delete"),
    
]