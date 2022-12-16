from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('all_stocks/', views.all_stocks, name="all_stocks"),
	path('stock/', views.stock, name="stock"),
	path('add_stock/', views.add_stock, name="add_stock"),
	path('remove_stock/<stock_id>', views.remove_stock, name="remove_stock"),
]