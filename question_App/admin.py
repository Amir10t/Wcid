from django.contrib import admin
from .models import QuestionModel, QuestionCategoryModel

# Register your models here.

admin.site.register(QuestionModel)
admin.site.register(QuestionCategoryModel)
