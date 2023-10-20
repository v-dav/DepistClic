from django.contrib import admin
from .models import Question, Comment, ScreeningTest

# Register your models here.
admin.site.register(Question)
admin.site.register(ScreeningTest)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_area', 'date')


admin.site.register(Comment, CommentAdmin)
