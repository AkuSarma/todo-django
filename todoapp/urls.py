from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home-page"),
    path('register/', views.register, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('delete-task/<int:id>/', views.deleteTask, name="deleteTask"),
    path('update-task/<int:id>/', views.updateTask, name= "updateTask"),
]
