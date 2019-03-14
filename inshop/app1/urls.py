from django.conf.urls import include, url
from . import views
from django.conf import settings


urlpatterns = [
     url(r'^$', views.HomePage.as_view(), name="bits in bytes"),
     url(r'product/(?P<pk>\d+)/$', views.product_details, name="product_details")
]
