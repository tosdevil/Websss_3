from django.shortcuts import render
from .models import Photo, Comment
from .forms import CommentForm

from django.views.generic.detail import DetailView

from django.views.generic import UpdateView, DeleteView, CreateView

# Create your views here.

def gallery(request):
    photos = Photo.objects.all()
    comments = Comment.objects.all()
    return render(request, 'gallery_app/gallery_home.html', {'photos': photos,'comments': comments})
		
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

class LeaveComment(CreateView):
    model = Comment
    template_name = 'gallery_app/leave_comment.html'
    form_class = CommentForm

    success_url = '/gallery/'

    def form_valid(self, form):
        form.instance.photo_id = self.kwargs['pk']
        return super(LeaveComment, self).form_valid(form)