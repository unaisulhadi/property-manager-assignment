from django.db import models
from django.utils import timezone

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Unit(models.Model):


    class UnitStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        OCCUPIED = 'OCCUPIED', 'Occupied'


    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=255)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=UnitStatus.choices, default=UnitStatus.AVAILABLE)

    def __str__(self):
        return f"{self.property.name} - {self.unit_number}"

class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def is_active(self):
        return self.start_date <= timezone.now().date() <= self.end_date

    def total_rent(self):
        return self.monthly_rent * (self.end_date - self.start_date).days / 30

    def __str__(self):
        return f"{self.member} - {self.unit.property} - {self.unit}"