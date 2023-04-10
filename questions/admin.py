from django.contrib import admin
from .models import Question, Answers
# Register your models here.



class AnswersAdmin(admin.ModelAdmin):
    list_display = ['answer','is_correct']


admin.site.register(Question)
admin.site.register(Answers,AnswersAdmin)