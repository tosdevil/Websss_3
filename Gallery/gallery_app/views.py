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
    def get_context_data(self, **kwargs):
      context = super(CommentView, self).get_context_data(**kwargs)
      context['comments_list'] = Comment.objects.all()
      return context
    # comments = Comment.objects.all()
    # 'comments': comments