from rest_framework import serializers
from .models import Post,Category,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','category','body','author','is_enabled', 'created_time','status','likes',)
        model=Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=('title',)
        model=Category


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('Post','text',)
        model=Comment