from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/', views.products_see, name='products_see'),
    path('products/<int:pk>/edit/', views.products_edit, name='products_edit'),
    path('products/<int:pk>/dell/', views.products_dell, name='products_dell'),
    path('days/', views.days, name='days'),
    path('days/days_free/', views.days_free, name='days_free'),
    path('days/days_cost/', views.days_cost, name='days_cost'),
]