from django.shortcuts import render

from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


def index(request):
    message = "Front-end under construction :)"
    context = {'message': message}
    return render(request, 'sentiment/index.html', context)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('post-list', request=request, format=format),
        'comments': reverse('comment-list', request=request, format=format)
    })


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



