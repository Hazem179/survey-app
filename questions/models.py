from django.db import models

# Create your models here.


class Question(models.Model):
    name = models.CharField(max_length=100,verbose_name="السؤال")
    description = models.TextField(null=True, blank=True,verbose_name="الوصف")
    attachment = models.FileField(upload_to='attachments', null=True, blank=True,verbose_name="الملفات المرفقة")
    def __str__(self):
        return self.name


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100,verbose_name="السؤال")
    is_correct = models.BooleanField(default=False,verbose_name="الإجابة الصحيحة")
    def __str__(self):
        return self.answer