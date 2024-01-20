from django.contrib import admin
from .models import QuestionModel, QuestionCategoryModel

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','category', 'is_active']
    list_editable = ['category', 'is_active']
    list_filter = ['category', 'is_active']

class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']

admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(QuestionCategoryModel, QuestionCategoryAdmin)
