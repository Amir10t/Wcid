from django.db import models

# Create your models here.

class QuestionCategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name="نام دسته بندی")
    url_title = models.CharField(max_length=50, verbose_name="عنوان انگلیسی")

    def __str__(self):
        return f"{self.title} -> {self.url_title}"

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دیسته بندی ها"

class QuestionModel(models.Model):
    question = models.CharField(max_length=300, verbose_name="سوال")
    option1 = models.CharField(max_length=20, verbose_name="گزینه 1")
    option2 = models.CharField(max_length=20, verbose_name="گزینه 2")
    option3 = models.CharField(max_length=20, verbose_name="گزینه 3")
    option4 = models.CharField(max_length=20, verbose_name="گزینه 4")
    category = models.ForeignKey(QuestionCategoryModel, on_delete=models.CASCADE, related_name="question_category", verbose_name='دسته بندی', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.question
    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"