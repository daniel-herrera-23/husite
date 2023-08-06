from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator



# Create your views here.
from .forms import HuertoForm, HuertoImageFormSet, HuertoVideoFormSet
from .models import Huerto

from .models import Testimonial
from .forms import TestimonialForm

from .models import BlogPost
from .forms import BlogPostForm

def huerto_list(request):
    huertos = Huerto.objects.all()
    context = {
        'huertos': huertos
    }
    return render(request, 'huertourbano/huerto_list.html', context)

import random
def landing(request):
   huertos = Huerto.objects.all()

   testimonials = Testimonial.objects.filter(is_visible=True)
   shuffled_testimonials = random.sample(list(testimonials), min(len(testimonials), 3))
   context = {
        'huertos': huertos,
        'testimonials': shuffled_testimonials,
         'featured_article' : BlogPost.objects.filter(is_featured=True).first()
    }
   return render(request, 'huertourbano/landing_page.html',context)














def huerto_detail(request, huerto_id):
    huerto = get_object_or_404(Huerto, id=huerto_id)
    image_formset = HuertoImageFormSet(instance=huerto)

    if request.method == 'POST':
        formset = HuertoImageFormSet(request.POST, request.FILES, instance=huerto)
        if formset.is_valid():
            formset.save()
            # Handle successful form submission, e.g., redirect to a success page
        else:
            print(formset.errors)  # Print formset errors for debugging

    context = {
        'huerto': huerto,
        'image_formset': image_formset,
    }
    return render(request, 'huertourbano/huerto_detail.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Huerto
from .forms import HuertoImageFormSet, HuertoVideoFormSet

def huerto_detail(request, huerto_id):
    huerto = get_object_or_404(Huerto, id=huerto_id)

    image_formset = HuertoImageFormSet(instance=huerto)
    video_formset = HuertoVideoFormSet(instance=huerto)

    context = {
        'huerto': huerto,
        'image_formset': image_formset,
        'video_formset': video_formset,
    }
    return render(request, 'huertourbano/huerto_detail.html', context)


from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import HuertoForm, HuertoImageForm, HuertoVideoForm

def add_huerto(request):
    if request.method == 'POST':
        form = HuertoForm(request.POST)
        image_formset = HuertoImageFormSet(request.POST, request.FILES, prefix='images')
        video_formset = HuertoVideoFormSet(request.POST, prefix='videos')

        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid():
            huerto = form.save()

            for image_form in image_formset:
                if image_form.cleaned_data.get('image'):
                    image = image_form.save(commit=False)
                    image.huerto = huerto
                    image.save()

            for video_form in video_formset:
                if video_form.cleaned_data.get('video_url'):
                    video = video_form.save(commit=False)
                    video.huerto = huerto
                    video.save()

            return redirect('huerto_list')
    else:
        form = HuertoForm()
        image_formset = HuertoImageFormSet(prefix='images')
        video_formset = HuertoVideoFormSet(prefix='videos')

    context = {
        'form': form,
        'image_formset': image_formset,
        'video_formset': video_formset,
    }
    return render(request, 'huertourbano/add_huerto.html', context)



def por_donde_empezar_view(request):
    # Add your logic for the "Por donde empezar" page view here
    return render(request, 'huertourbano/por_donde_empezar.html')

def tecnicas_de_cultivo_view(request):
    # Add your logic for the "Tecnicas de Cultivo" page view here
    return render(request, 'huertourbano/tecnicas_de_cultivo.html')

def cuida_tu_huerto_view(request):
    # Add your logic for the "Cuida tu huerto" page view here
    return render(request, 'huertourbano/cuida_tu_huerto.html')




#import random
def add_testimonials_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('testimonials')

    else:
        form = TestimonialForm()

    # Retrieve only visible testimonials from the database
    testimonials = Testimonial.objects.filter(is_visible=True)

    context = {'testimonials': testimonials, 'form': form}
    return render(request, 'add_testimonial.html', context)




#def add_testimonials_view(request):
#    # ... your existing code ...

 #   # Retrieve all visible testimonials from the database
 #   testimonials = Testimonial.objects.filter(is_visible=True)

 #   # Shuffle the testimonials randomly
 #   random.shuffle(testimonials)

 #   context = {'testimonials': testimonials, 'form': form}
 #   return render(request, 'testimonials.html', context)







def testimonials_view(request):
    # Retrieve all visible testimonials from the database
    testimonials = Testimonial.objects.filter(is_visible=True)

    # Initialize the paginator with the testimonials and the number of items per page (10 in this case)
    paginator = Paginator(testimonials, 10)

    # Get the current page number from the request's query parameters, default to 1
    page_number = request.GET.get('page', 1)

    try:
        # Get the testimonials for the current page
        current_page = paginator.page(page_number)
    except EmptyPage:
        # If the page number is out of range, show the first page
        current_page = paginator.page(1)

    context = {'current_page': current_page}
    return render(request, 'testimonials.html', context)


from django.shortcuts import render

def about_view(request):
    return render(request, 'huertourbano/about.html')


def alianzas_view(request):
    #add info de alianzas
    return render(request, 'huertourbano/alianzas.html')


def contacto_view(request):
    #add info de contacto
    return render(request, 'huertourbano/contacto.html')

def propuesta_view(request):
    #add info de propuesta
    return render(request, 'huertourbano/propuesta.html')












def blog_list(request):
    # View for listing all blog posts
    blog_posts = BlogPost.objects.all()
    return render(request, 'huertourbano/blog_list.html', {'blog_posts': blog_posts})

def blog_detail(request, pk):
    # View for displaying individual blog post
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'huertourbano/blog_detail.html', {'blog_post': blog_post})

def create_blog_post(request):
    # View for creating a new blog post
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'huertourbano/create_blog_post.html', {'form': form})

def edit_blog_post(request, pk):
    # View for editing an existing blog post
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'huertourbano/edit_blog_post.html', {'form': form})




