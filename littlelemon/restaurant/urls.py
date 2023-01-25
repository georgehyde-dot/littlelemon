from django.contrib import admin 
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, BookingViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [ 
   
    path('', views.index, name='home'),
    path('menu/', views.MenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]