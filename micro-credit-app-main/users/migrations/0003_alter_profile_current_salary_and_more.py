# Generated by Django 4.2.4 on 2023-09-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_current_emis_alter_profile_house_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_salary',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grocery_expense',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_hike_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='previous_salary',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
