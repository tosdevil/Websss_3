from django.urls import path
from . import views
from .views import CommentView, LeaveComment

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<int:pk>/', CommentView.as_view(), name = 'commentview'),
    path('photo/add_comment/<int:pk>', LeaveComment.as_view(), name = 'add_comment')
]