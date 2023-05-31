from django.shortcuts import render
from .models import Photo, Comment

from django.views.generic.detail import DetailView

# Create your views here.

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery_app/gallery_home.html', {'photos': photos})
		
class CommentView(DetailView):
    model = Photo
    context_object_name = 'commentview'
    template_name = 'gallery_app/photo.html'
    # comments = Comment.objects.all()
    # 'comments': comments