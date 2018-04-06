from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^/cylligraphy/contact', views.contact, name="contact")
]