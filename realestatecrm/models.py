from django.db import models

# Create your models here.

class Realestate(models.Model):

    address=models.TextField()

    price=models.PositiveIntegerField()

    property_option=(
        ("apartment","apartment"),

        ("house","house"),

        ("land","land"),
    )

    property_type=models.CharField(max_length=200,choices=property_option,default="land")

    number_of_bedroom=models.PositiveIntegerField()

    square_footage=models.PositiveIntegerField()

    location_option=(
        ("city","city"),

        ("neighbourhood","neighbourhood"),
    )

    location=models.CharField(max_length=200,choices=location_option,default="city")

    picture=models.ImageField(upload_to="realestate_images",null=True,blank=True)

    contact=models.CharField(max_length=200)

    def __str__(self):

        return self.name

