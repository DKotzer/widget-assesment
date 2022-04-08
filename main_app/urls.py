from django.urls import path
from . import views
from .models import Widget


urlpatterns = [
  
    path('widgets/', views.widgets, name="widgets"),
    path('widgets/add_widget/<int:pk>', views.add_widget, name='add_widget'),
    
]