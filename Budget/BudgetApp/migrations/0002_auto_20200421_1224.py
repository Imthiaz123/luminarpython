# Generated by Django 3.0.5 on 2020-04-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BudgetApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
    ]
