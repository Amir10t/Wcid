# Generated by Django 5.0 on 2024-01-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question_App", "0006_alter_questionmodel_option1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionmodel",
            name="question",
            field=models.TextField(max_length=300, verbose_name="سوال"),
        ),
    ]
