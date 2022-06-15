from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.super_detail),
    path('<int:pk>/<int:id>/', views.add_power),
]