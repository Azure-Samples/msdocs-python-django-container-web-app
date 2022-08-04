from django.urls import path, register_converter
from restaurant_review import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>/', views.details, name='details'),
    path('create', views.create_restaurant, name='create_restaurant'),
    path('add', views.add_restaurant, name='add_restaurant'),
    path('review/<str:id>', views.add_review, name='add_review'),
]