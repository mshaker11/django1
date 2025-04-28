from django.contrib import admin
from django.urls import path  # <-- THIS is what you were missing
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.createItem, name='create'),
    path('update/<str:pk>/', views.updateItem, name='update'),
    path('delete/<str:pk>/', views.deleteItem, name='delete'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('rooms/', views.roomList, name='room-list'),
    path('rooms/create/', views.createRoom, name='create-room'),
    path('rooms/update/<str:pk>/', views.updateRoom, name='update-room'),
    path('rooms/delete/<str:pk>/', views.deleteRoom, name='delete-room'),
     path('activity/', views.activityFeed, name='activity-feed'),
     path('profile/<str:pk>/', views.profileUser, name='profile'),
     path('account/edit/', views.editAccount, name='edit-account'),
]

