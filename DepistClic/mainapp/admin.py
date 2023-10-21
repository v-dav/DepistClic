from django.contrib import admin
from .models import Question, Comment, ScreeningTest
from django.forms import Textarea
from django.db import models



# Register your models here.
admin.site.register(Question)
admin.site.register(ScreeningTest)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_area', 'date')


# class ScreeningTestAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.JSONField: {'widget': Textarea(attrs={'rows': 8, 'cols': 40})},
#     }


admin.site.register(Comment, CommentAdmin)
