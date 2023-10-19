from django.contrib import admin
from .models import Question, Comment

# Register your models here.
admin.site.register(Question)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_area', 'date')

admin.site.register(Comment, CommentAdmin)