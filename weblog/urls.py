from django.urls import path

from .views import PostDetail, PostList ,CategoryList,CategoryDetail, CommentList,CommentDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(),name="post detail"),
    path('', PostList.as_view(),name="post list"),
    path('CategoryList/',CategoryList.as_view(),name="category"),
    path('<int:pk>/',CategoryDetail.as_view(),name="category detail"),
    path('CommentList/',CommentList.as_view(),name="comment list"),
    path('<int:pk>/',CommentDetail.as_view(),name="comment detail"),
]
