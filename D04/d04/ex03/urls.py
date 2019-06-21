from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^django/', views.ex03_django),
]