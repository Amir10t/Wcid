# Generated by Django 5.0 on 2023-12-16 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question_App", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionCategoryModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=50, verbose_name="نام دسته بندی"),
                ),
                (
                    "url_title",
                    models.CharField(max_length=50, verbose_name="عنوان انگلیسی"),
                ),
            ],
            options={
                "verbose_name": "دسته بندی",
                "verbose_name_plural": "دیسته بندی ها",
            },
        ),
        migrations.AlterModelOptions(
            name="questionmodel",
            options={"verbose_name": "سوال", "verbose_name_plural": "سوالات"},
        ),
        migrations.RemoveField(
            model_name="questionmodel",
            name="is_delete",
        ),
        migrations.AddField(
            model_name="questionmodel",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question_category",
                to="question_App.questioncategorymodel",
                verbose_name="دسته بندی",
            ),
        ),
    ]
