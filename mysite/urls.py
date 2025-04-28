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
]
