"""
URL configuration for husite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from huertourbano import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing, name='landing'),


    path('por-donde-empezar/', views.por_donde_empezar_view, name='por_donde_empezar'),
    path('tecnicas-de-cultivo/', views.tecnicas_de_cultivo_view, name='tecnicas_de_cultivo'),
    path('cuida-tu-huerto/', views.cuida_tu_huerto_view, name='cuida_tu_huerto'),

    path('huertos/', views.huerto_list, name='huerto_list'),
    path('huertos/<int:huerto_id>/', views.huerto_detail, name='huerto_detail'),
    path('huertos/add/', views.add_huerto, name='add_huerto'),
    path('huertos/testimonials/', views.testimonials_view, name='testimonials'),

    path('huertos/create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('huertos/blog_list/', views.blog_list, name='blog_list'),
    path('', include('huertourbano.urls')),



    path('add_testimonials/', views.add_testimonials_view, name='add_testimonials'),
    path('about/', views.about_view, name='about'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('alianzas/', views.alianzas_view, name='alianzas'),
    path('propuesta/', views.propuesta_view, name='propuesta'),
]


if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)