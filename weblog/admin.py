from django.contrib import admin

from .models import Category,Post,Comment

class CommentAdminInline(admin.TabularInline):
    model=Comment
    fields=['text',]
    extra=0


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','active']

class PostAdmin(admin.ModelAdmin):
    list_display=['title','category','publish_time','status','likes','dislikes',]
    search_fields=('title','body')
    list_filter=('status','publish_time')
    date_hierarchy= 'publish_time'
    likes=('likes',)
    dislikes=('dislikes',)
    Featured=('Featured',)
    Comment=('Comment',)
    inlines=[CommentAdminInline,]

# class CommentAdmin (admin.ModelAdmin):
#     list_display=['Post','text','created_time']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

# admin.site.register(Comment,CommentAdmin)