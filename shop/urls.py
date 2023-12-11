from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.shop, name='shop'),
                  path('add-product', views.add_product, name='add-product'),
                  path('edit-product/<slug:prod_slug>', views.edit_product, name='edit-product'),
                  path('success', views.success, name='order-success'),
                  path('<slug:category_slug>', views.shop_category, name='category'),
                  path('<slug:category_slug>/<slug:prod_slug>', views.one_item, name='one-item'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)

