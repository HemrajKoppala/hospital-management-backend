from django.db import models
from django.conf import settings


class Doctor(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    qualification = models.CharField(max_length=100)

    experience = models.PositiveIntegerField()

    phone = models.CharField(max_length=15)

    department = models.CharField(max_length=100)

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name