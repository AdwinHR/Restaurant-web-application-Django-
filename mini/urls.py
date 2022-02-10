
from django.urls import path ,include
from . import views
from .views import home,register
urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),

]
