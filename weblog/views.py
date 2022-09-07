from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Post,Category,Comment
from .serializers import PostSerializer,CategorySerializer,CommentSerializer 


class PostList(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer


class CategoryList(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Category.objects.all()
    serializer_class= CategorySerializer

class CategoryDetail(generics.RetrieveDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer 



class CommentDetail(generics.RetrieveDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer