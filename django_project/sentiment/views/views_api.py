from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers import PostSerializer, CommentSerializer
from ..models import Post, Comment


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


class CommentsByPostList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def paginate_queryset(self, queryset, view=None):
        # couldn't find a better solution
        return None

    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        post = self.kwargs['idpost']
        return Comment.objects.filter(idpost=post)



