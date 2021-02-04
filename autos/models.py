from django.db import models
from django.core.validators import MinLengthValidator

class Make(models.Model):
    name=models.CharField(
        max_length=200,
        help_text='Enter a make (ex Peugeot)',
        validators=[MinLengthValidator(2,"Make must be greater than 2 characters")]
    )

    def __str__(self):
        """String for representing the Model objects"""
        return self.name

class Auto(models.Model):
    nickname= models.CharField(
        max_length=200,
        help_text='Enter a nickname for the car',
        validators=[MinLengthValidator(2,"Nickname must be greater than 2 char")]
    )

    mileage=models.PositiveIntegerField()
    comments=models.CharField(max_length=300)
    make=models.ForeignKey('Make',on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname


# Create your models here.
