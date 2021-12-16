
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="main-home"),
    path('item/<int:pk>', views.todo, name="todo"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('view/', views.view, name="view"),
]
