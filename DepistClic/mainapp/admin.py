from django.contrib import admin
from .models import Question, Comment, ScreeningTest


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('order', 'response_type', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_area', 'date')


class ScreeningTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'frequency', 'type')


admin.site.register(Question, QuestionAdmin)
admin.site.register(ScreeningTest, ScreeningTestAdmin)
admin.site.register(Comment, CommentAdmin)
