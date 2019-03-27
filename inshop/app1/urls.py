from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     url(r'^$', views.HomePage.as_view(), name="bits in bytes"),
     url(r'product/(?P<pk>\d+)/$', views.product_details, name="product_details"),
     url(r'account/profile/$', views.Profile.as_view(), name="profile"),
     url(r'account/profile/change_data$', views.user_change_info, name="profile_correct"),
     url(r'account/basket$', views.basket, name="basket"),
     url(r'account/basket/(?P<pk>\d+)$', views.basket, name="basket"),
     url(r'search/$', views.Search.as_view(), name='searching'),
     url(r'account/basket/buy_one/(?P<pk>\d+)$', views.buy_one_product, name="product_buy_one"),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
