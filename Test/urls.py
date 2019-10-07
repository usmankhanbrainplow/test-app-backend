from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^pro_get_post/$', views.product_get_post),
url(r'^pro_edit_delete/(?P<id>.+)$',views.product_edit_delete),
]