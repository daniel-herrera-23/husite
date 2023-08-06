from django.contrib import admin

# Register your models here.
from .models import Huerto, HuertoImage, HuertoVideo, Testimonial, BlogPost

admin.site.register(Huerto)

admin.site.register(HuertoImage)
admin.site.register(HuertoVideo)
admin.site.register(Testimonial)
admin.site.register(BlogPost)