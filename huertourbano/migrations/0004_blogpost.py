# Generated by Django 4.2 on 2023-08-03 04:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huertourbano', '0003_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('leading_image', models.ImageField(upload_to='blog/images/')),
                ('body', ckeditor.fields.RichTextField()),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]