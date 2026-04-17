from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Unit(models.Model):
    class UnitStatus(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        OCCUPIED = "OCCUPIED", "Occupied"

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=255)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=255, choices=UnitStatus.choices, default=UnitStatus.AVAILABLE
    )

    def __str__(self):
        return f"{self.property.name} - {self.unit_number}"
