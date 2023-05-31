from django.urls import path
from . import views
from .views import CommentView

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<int:pk>/', CommentView.as_view(), name = 'commentview')
]