from django.db import models
from django.conf import settings


class Patient(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    gender = models.CharField(max_length=20)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    blood_group = models.CharField(
        max_length=5,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name