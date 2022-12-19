from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('all_stocks/', views.all_stocks, name="all_stocks"),
	path('stock/', views.stock, name="stock"),
	path('stock/<str:ticker>/', views.stock, name="stock_info"),
	path('add_stock/<str:ticker>', views.add_stock, name="add_stock"),
	path('remove_stock/<str:ticker>', views.remove_stock, name="remove_stock"),
	path('remove_stock/<stock_id>', views.remove_stock, name="remove_stock"),
	path('portfolio/', views.portfolio, name="portfolio"),
	path('register/', views.register_request, name="register"),
]