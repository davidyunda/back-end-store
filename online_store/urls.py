from django.urls import path
from . import views
from .views import RoomView

urlpatterns = [
    
    path('api/', RoomView.as_view()),
    path('', views.home, name='home'),
    path('data', views.getData, name='getData' )
]
