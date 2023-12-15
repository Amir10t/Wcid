from django.db import models

# Create your models here.

class QuestionModel(models.Model):
    question = models.CharField(max_length=300, verbose_name="سوال")
    option1 = models.CharField(max_length=20, verbose_name="گزینه 1")
    option2 = models.CharField(max_length=20, verbose_name="گزینه 2")
    option3 = models.CharField(max_length=20, verbose_name="گزینه 3")
    option4 = models.CharField(max_length=20, verbose_name="گزینه 4")
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')