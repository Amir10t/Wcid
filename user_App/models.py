from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PersonModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_person",
        verbose_name="کاربر"
    )
    ability = models.CharField(max_length=300, null=True, blank=True, verbose_name="توانایی های کاربر")
    favorite = models.CharField(max_length=300, null=True, blank=True, verbose_name="علاقه های کاربر")
    review = models.CharField(max_length=300, null=True, blank=True, verbose_name="ارزیابی کلی")

    def __str__(self):
        return f"{self.user} -> {self.ability}"

    class Meta:
        verbose_name = "بررسی شخصیتی"
        verbose_name_plural = "بررسی های شخصیت ها"