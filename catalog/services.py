from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = list(Product.objects.all())
    cache.set(key, products, timeout=3600)
    return products


def get_products_by_category(category_name: str):
    return Product.objects.filter(category__name=category_name).all()