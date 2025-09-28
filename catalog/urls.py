from django.urls import path
from .views import (
    HomeView,
    ContactsView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsByCategoryView
)
from django.views.decorators.cache import cache_page

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/',cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<str:category_name>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]
