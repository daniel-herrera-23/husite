from django.urls import path

from .views import huerto_detail

urlpatterns = [
    path("", huerto_detail, name='huerto_detail'),
] 