# Generated by Django 4.2.4 on 2023-09-18 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=140)),
                ('address', models.TextField(blank=True)),
                ('pan_number', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=140)),
                ('current_salary', models.PositiveIntegerField()),
                ('previous_salary', models.PositiveIntegerField()),
                ('own_house', models.BooleanField()),
                ('house_rent', models.PositiveIntegerField()),
                ('grocery_expense', models.PositiveIntegerField()),
                ('current_emis', models.PositiveIntegerField()),
                ('last_hike_date', models.DateField()),
                ('other_expenses', models.PositiveIntegerField()),
                ('risk_score', models.IntegerField()),
                ('is_approved', models.BooleanField()),
                ('loan_granted', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
