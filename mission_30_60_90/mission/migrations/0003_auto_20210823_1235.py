# Generated by Django 3.1.3 on 2021-08-23 07:05

from django.db import migrations, models
import mission.validate


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0002_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missions',
            name='no_of_days',
            field=models.IntegerField(validators=[mission.validate.validate_days]),
        ),
    ]