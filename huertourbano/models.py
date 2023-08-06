from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Huerto(models.Model):
    ESTADO_CHOICES = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )

    cultivo = models.CharField(max_length=255)
    caracteristicas = models.CharField(max_length=1000)
    nutrientes = models.CharField(max_length=255)
    procsiembra = models.CharField(max_length=1000)
    cuidados = models.CharField(max_length=1000)
    requerimientos = models.CharField(max_length=1000)
    cosecha = models.CharField(max_length=1000)
    estado = models.CharField(max_length=25, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.cultivo


class HuertoImage(models.Model):
    huerto = models.ForeignKey(Huerto, on_delete=models.CASCADE, related_name='images')
    descripcion = models.CharField(max_length=255)
    image = models.ImageField(upload_to='huerto_images/')

    def __str__(self):
        return self.descripcion


class HuertoVideo(models.Model):
    huerto = models.ForeignKey(Huerto, on_delete=models.CASCADE, related_name='videos')
    descripcion = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.descripcion




class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)  # Add the is_visible field

    def __str__(self):
        return f"{self.author}: {self.quote}"



# models.py


# models.py


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateField()
    leading_image = models.ImageField(upload_to='blog/images/')
    body = RichTextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

