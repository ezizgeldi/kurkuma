    from  .views import base_view, product_view, category_view
from django.urls import path


urlpatterns = [
    path("", base_view, name="base_view"),
    path("category/(?P<category_slug>[-\w]+)/", category_view, name = 'category_detail'),
    path("product/(?P<product_slug>[-\w]+)/", product_view, name='product_detail')
]
