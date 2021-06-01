from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Male', _('Male')
        FEMALE = 'Female', _('Female')
        UNDEFINED = 'UND', _('Undefined')

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=144)
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices,
        default=Gender.MALE,
    )
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __str__(self):
        return self.email
