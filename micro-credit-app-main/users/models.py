from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=140, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    company = models.CharField(max_length=140, blank=True, null=True)
    current_salary = models.PositiveIntegerField(blank=True, null=True)
    previous_salary = models.PositiveIntegerField(blank=True, null=True)
    own_house = models.BooleanField(blank=True, null=True)
    house_rent = models.PositiveIntegerField(blank=True, null=True)
    grocery_expense = models.PositiveIntegerField(blank=True, null=True)
    current_emis = models.PositiveIntegerField(blank=True, null=True)
    last_hike_date = models.DateField(blank=True, null=True)
    other_expenses = models.PositiveIntegerField(blank=True, null=True)
    risk_score = models.IntegerField(blank=True, null=True)
    is_approved = models.BooleanField(blank=True, null=True)
    loan_granted = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
