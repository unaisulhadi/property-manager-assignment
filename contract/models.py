from django.db import models

from property.models import Unit
from member.models import Member
from django.utils import timezone


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
