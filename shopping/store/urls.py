from django.urls import path
from . import views

urlpatterns = [
    # path('/home',views.home, name='home'),
    # Add more patterns as needed

    path('', views.home, name='home')
]
