from django import forms
from .models import Huerto, HuertoImage, HuertoVideo, BlogPost
from django.forms import inlineformset_factory
from .models import Testimonial





class HuertoForm(forms.ModelForm):
    class Meta:
        model = Huerto
        fields = '__all__'



class HuertoImageForm(forms.ModelForm):
    class Meta:
        model = HuertoImage
        fields = ('image', 'descripcion')

HuertoImageFormSet = inlineformset_factory(Huerto, HuertoImage, form=HuertoImageForm, extra=1)

class HuertoVideoForm(forms.ModelForm):
    class Meta:
        model = HuertoVideo
        fields = ('video_url', 'descripcion')

HuertoVideoFormSet = inlineformset_factory(Huerto, HuertoVideo, form=HuertoVideoForm, extra=1)



class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['quote', 'author', 'is_visible']  # Include the is_visible field in the form





class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'pub_date', 'leading_image', 'body', 'is_featured']




