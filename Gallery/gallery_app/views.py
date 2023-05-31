from django.shortcuts import render
from .models import Photo

# Create your views here.

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery_app/gallery_home.html', {'photos': photos})
		