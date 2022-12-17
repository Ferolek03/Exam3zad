from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
                  path('', Index.as_view(), name='index'),
                  path('products', Products.as_view(), name='product'),
                  path('about', About.as_view(), name='about'),
                  path('contacts', Contact.as_view(), name='contact'),
                  path('add_product', AddProduct.as_view(), name='add_product'),
                  path('login', Login.as_view(), name='login'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
