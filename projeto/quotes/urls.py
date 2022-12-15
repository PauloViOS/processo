from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('all_stocks/', views.all_stocks, name="all_stocks"),
	path('stock/', views.stock, name="stock"),
]